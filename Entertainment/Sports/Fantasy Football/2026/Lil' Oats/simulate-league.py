"""Lil' Oats 2026 fixed-roster Monte Carlo from a saved Sleeper snapshot."""
import json
from pathlib import Path

import numpy as np

SEED = 20260911
N = 200_000
WEEKS = 16  # 14 regular-season weeks, Week 15 semifinal, Week 16 final.
BATCH = 5_000

DATA = json.loads(Path(__file__).with_name("league-simulation-inputs.json").read_text())
PLAYERS = DATA["players"]
ROSTERS = DATA["rosters"]
NAMES = {r["roster_id"]: r["name"] for r in ROSTERS}

all_ids = sorted({p for r in ROSTERS for p in r["players"]})
pid_to_i = {p: i for i, p in enumerate(all_ids)}
P = len(all_ids)

means = np.zeros((WEEKS, P), dtype=float)
teams = []
positions = []
full_names = []
for p in all_ids:
    d = PLAYERS.get(p, {})
    fantasy_positions = d.get("fantasy_positions") or []
    # Use offensive eligibility for Hunter's DB/WR dual designation.
    pos = next((x for x in fantasy_positions if x in {"QB", "RB", "WR", "TE", "K", "DEF"}), None)
    if p.isalpha() and len(p) <= 3:
        pos = "DEF"
    positions.append(pos or d.get("position") or "UNK")
    teams.append(d.get("team") or (p if positions[-1] == "DEF" else "FA"))
    full_names.append(d.get("full_name") or p)

for w in range(1, WEEKS + 1):
    by_id = DATA["projections_half_ppr"][str(w)]
    for p, i in pid_to_i.items():
        v = by_id.get(p)
        means[w - 1, i] = max(0.0, float(v)) if v is not None else 0.0

roster_indices = {r["roster_id"]: np.array([pid_to_i[p] for p in r["players"]]) for r in ROSTERS}
starter_indices = {r["roster_id"]: np.array([pid_to_i[p] for p in r["starters"]]) for r in ROSTERS}
schedule = {int(w): [tuple(pair) for pair in pairs] for w, pairs in DATA["schedule"].items()}
posted = {pid_to_i[p]: float(score) for p, score in DATA["week_1_posted_nonzero_starter_points"].items()}

pos_cv = {"QB": .38, "RB": .62, "WR": .70, "TE": .72, "K": .52, "DEF": .80}
cv = np.array([pos_cv.get(x, .70) for x in positions])
shape = 1 / cv**2
scale = cv**2

# Weekly new-injury hazards and absence durations are transparent model assumptions.
hazard = np.array([{"QB": .008, "RB": .026, "WR": .020, "TE": .020, "K": .004, "DEF": 0}.get(x, .02) for x in positions])
durations = np.array([1, 2, 3, 4, 6])
duration_prob = np.array([.55, .23, .10, .07, .05])

nfl_teams = sorted(set(teams))
team_to_i = {t: i for i, t in enumerate(nfl_teams)}
player_team_i = np.array([team_to_i[t] for t in teams])

rank_counts = np.zeros((8, 8), dtype=np.int64)
playoff_counts = np.zeros(8, dtype=np.int64)
champ_counts = np.zeros(8, dtype=np.int64)
runner_counts = np.zeros(8, dtype=np.int64)
wins_sum = np.zeros(8)
wins_hist = np.zeros((8, 15), dtype=np.int64)
points_sum = np.zeros(8)
score_sum = np.zeros((8, WEEKS))
week_win_counts = np.zeros((8, 14), dtype=np.int64)

def select_lineup(rid, week, available, forecast, actual, fixed_week1=False):
    """Return scores for each simulation using legal lineup slots and known availability."""
    b = actual.shape[0]
    if fixed_week1:
        chosen = starter_indices[rid]
        out = actual[:, chosen].sum(axis=1)
        for i in chosen:
            if i in posted:
                out += posted[i] - actual[:, i]
        return out
    ids = roster_indices[rid]
    chosen = np.zeros((b, P), dtype=bool)
    for pos, count in (("QB", 1), ("RB", 2), ("WR", 2), ("TE", 1), ("K", 1), ("DEF", 1)):
        cand = np.array([i for i in ids if positions[i] == pos], dtype=int)
        if not len(cand):
            continue
        vals = np.where(available[:, cand], forecast[:, cand], -1.0)
        take = min(count, len(cand))
        order = np.argpartition(vals, -take, axis=1)[:, -take:]
        for k in range(take):
            ci = cand[order[:, k]]
            valid = vals[np.arange(b), order[:, k]] >= 0
            chosen[np.arange(b)[valid], ci[valid]] = True
    cand = np.array([i for i in ids if positions[i] in {"RB", "WR", "TE"}], dtype=int)
    if len(cand):
        vals = np.where(available[:, cand] & ~chosen[:, cand], forecast[:, cand], -1.0)
        order = vals.argmax(axis=1)
        valid = vals[np.arange(b), order] >= 0
        ci = cand[order]
        chosen[np.arange(b)[valid], ci[valid]] = True
    return (actual * chosen).sum(axis=1)

rng = np.random.default_rng(SEED)
done = 0
while done < N:
    b = min(BATCH, N - done)
    # Persistent season-long player projection error; mean normalized.
    talent = rng.lognormal(-.18**2 / 2, .18, size=(b, P))
    remaining = np.zeros((b, P), dtype=np.int16)
    weekly_team = rng.lognormal(-.12**2 / 2, .12, size=(b, WEEKS, len(nfl_teams)))
    scores = np.zeros((b, 8, WEEKS))
    for w in range(WEEKS):
        available = means[w][None, :] > 0
        available = np.broadcast_to(available, (b, P)).copy()
        if w > 0:
            new = (rng.random((b, P)) < hazard[None, :]) & (remaining == 0) & available
            if new.any():
                remaining[new] = rng.choice(durations, size=int(new.sum()), p=duration_prob)
            available &= remaining == 0
        env = weekly_team[:, w, :][:, player_team_i]
        weekly = rng.gamma(shape[None, :], scale[None, :], size=(b, P))
        actual = means[w][None, :] * talent * env * weekly * available
        # Managers see availability and use Sleeper projection plus a modest estimate of role strength.
        forecast = means[w][None, :] * np.sqrt(talent) * available
        for rid in range(1, 9):
            scores[:, rid - 1, w] = select_lineup(rid, w, available, forecast, actual, fixed_week1=(w == 0))
        if w > 0:
            remaining = np.maximum(remaining - 1, 0)

    wins = np.zeros((b, 8), dtype=np.int32)
    for w in range(1, 15):
        for a, c in schedule[w]:
            sa, sc = scores[:, a - 1, w - 1], scores[:, c - 1, w - 1]
            wins[:, a - 1] += sa > sc
            wins[:, c - 1] += sc > sa
            week_win_counts[a - 1, w - 1] += int((sa > sc).sum())
            week_win_counts[c - 1, w - 1] += int((sc > sa).sum())
    pf = scores[:, :, :14].sum(axis=2)
    # Record first, points-for second. Random jitter only resolves exact remaining ties.
    key = wins * 10_000 + pf + rng.random((b, 8)) * 1e-6
    order = np.argsort(-key, axis=1)
    for rank in range(8):
        np.add.at(rank_counts[:, rank], order[:, rank], 1)
    top4 = order[:, :4]
    for k in range(4):
        np.add.at(playoff_counts, top4[:, k], 1)
    s1, s2, s3, s4 = [top4[:, k] for k in range(4)]
    rows = np.arange(b)
    semi1 = np.where(scores[rows, s1, 14] >= scores[rows, s4, 14], s1, s4)
    semi2 = np.where(scores[rows, s2, 14] >= scores[rows, s3, 14], s2, s3)
    champ = np.where(scores[rows, semi1, 15] >= scores[rows, semi2, 15], semi1, semi2)
    runner = np.where(champ == semi1, semi2, semi1)
    np.add.at(champ_counts, champ, 1)
    np.add.at(runner_counts, runner, 1)
    wins_sum += wins.sum(axis=0)
    for i in range(8):
        np.add.at(wins_hist[i], wins[:, i], 1)
    points_sum += pf.sum(axis=0)
    score_sum += scores.sum(axis=0)
    done += b

baseline = np.zeros((8, WEEKS))
for w in range(WEEKS):
    available = np.broadcast_to(means[w][None, :] > 0, (1, P)).copy()
    actual = means[w][None, :]
    for rid in range(1, 9):
        baseline[rid - 1, w] = select_lineup(rid, w, available, actual, actual, fixed_week1=(w == 0))[0]

out = {
    "seed": SEED,
    "simulations": N,
    "teams": [],
    "input_snapshot_date": DATA["snapshot_date"],
    "model": {
        "regular_weeks": 14,
        "playoff_weeks": [15, 16],
        "persistent_player_log_sd": .18,
        "nfl_team_week_log_sd": .12,
        "weekly_score_cv": pos_cv,
        "weekly_new_injury_hazard": {k: float(v) for k, v in zip(positions, hazard)},
        "injury_durations": dict(zip(map(str, durations), duration_prob)),
    },
}
for i in range(8):
    out["teams"].append({
        "roster_id": i + 1,
        "name": NAMES[i + 1],
        "baseline_lineup_ppg_w1_14": round(float(baseline[i, :14].mean()), 2),
        "sim_mean_points_w1_14": round(float(points_sum[i] / N), 2),
        "sim_mean_ppg_w1_14": round(float(points_sum[i] / N / 14), 2),
        "mean_wins": round(float(wins_sum[i] / N), 3),
        "record_win_count_pct": [round(float(x / N * 100), 2) for x in wins_hist[i]],
        "expected_regular_finish": round(float(sum((r + 1) * rank_counts[i, r] for r in range(8)) / N), 3),
        "week_1_win_pct": round(float(week_win_counts[i, 0] / N * 100), 2),
        "playoff_pct": round(float(playoff_counts[i] / N * 100), 2),
        "champ_pct": round(float(champ_counts[i] / N * 100), 2),
        "runner_up_pct": round(float(runner_counts[i] / N * 100), 2),
        "finish_pct": [round(float(x / N * 100), 2) for x in rank_counts[i]],
        "baseline_weekly": [round(float(x), 2) for x in baseline[i]],
    })
print(json.dumps(out, indent=2))
