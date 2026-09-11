"""Conditional scenario experiment, not a calibrated NFL forecast. Python + numpy."""
import json
from pathlib import Path
import numpy as np

N = 4000
W = 17
# Name, position, NFL team, screenshot Week 1 projection, bye.
DATA = [
 ('Allen','QB','BUF',17.56,7),('Price','RB','SEA',9,11),
 ('Montgomery','RB','HOU',14.25,8),('McConkey','WR','LAC',10.83,7),
 ('Jameson','WR','DET',12.02,6),('LaPorta','TE','DET',11.13,6),
 ('Lloyd','RB','GB',8.57,11),('Dicker','K','LAC',7.15,7),
 ('Rams','DEF','LAR',7,11),('Henderson','RB','NE',10,11),
 ('Wilson','WR','ARI',8.49,14),('Hunter','WR','JAX',2.96,7),
 ('Kincaid','TE','BUF',6.82,7),('Sadiq','TE','NYJ',3.49,13),
 ('Metcalf','WR','PIT',10,9),('Harrison','WR','ARI',8,14),
 ('Marks','RB','HOU',8,8)]
IDX={p[0]:i for i,p in enumerate(DATA)}
BASE=list(range(14))
def roster(drop,add):
 return [i for i in BASE if i!=IDX[drop]]+[IDX[add]]
POLICIES={'Hold':BASE,'Sadiq to Metcalf':roster('Sadiq','Metcalf'),
 'Wilson to Harrison':roster('Wilson','Harrison'),
 'Wilson to Marks':roster('Wilson','Marks'),
 'Hunter to Metcalf':roster('Hunter','Metcalf')}
PAIRS=[('Metcalf','Sadiq'),('Harrison','Wilson'),('Marks','Wilson'),('Metcalf','Hunter'),('Metcalf','Lloyd')]

def simulate(role,injury):
 rng=np.random.default_rng(20260911) # Common random numbers across assumptions and decisions.
 mu=np.tile(np.array([p[3] for p in DATA]),(N,W,1)).astype(float)
 # Three deliberately different worlds, equally weighted as a sensitivity test.
 settings={
 'screenshot':(8,8.49,10,3.49,2.96,4,8.57,14.25,8),
 'challengers':(12,7,10,6,7,2,9,10,12),
 'incumbents':(6.5,11,8,7,2,14,13,15,6)}
 h,wi,dk,sa,hu,dur,ll,mo,ma=settings[role]
 for name,value in [('Harrison',h),('Wilson',wi),('Metcalf',dk),('Sadiq',sa),('Hunter',hu),('Montgomery',mo),('Marks',ma)]:
  mu[:,:,IDX[name]]=value
 mu[:,:,IDX['Lloyd']]=np.where(np.arange(W)<dur,ll,4)
 # Unknown recovery lasts 1, 2, or 4 weeks; equal illustrative weights.
 recovery=rng.choice([1,2,4],N)
 # Persistent talent/role uncertainty, 25% lognormal SD, normalized mean.
 mu*=rng.lognormal(-.25**2/2,.25,(N,1,len(DATA)))
 # Negatively related shares for same-backfield / same-receiver-room pairs.
 for a,b in [('Montgomery','Marks'),('Harrison','Wilson')]:
  share=rng.uniform(-.25,.25,(N,1))
  mu[:,:,IDX[a]]*=1+share; mu[:,:,IDX[b]]*=1-share
 available=np.ones_like(mu,dtype=bool)
 hazard={'low':.012,'medium':.025,'high':.045}[injury]
 for p,(_,pos,team,_,bye) in enumerate(DATA):
  remaining=np.zeros(N,dtype=int)
  for week in range(W):
   hit=(rng.random(N)<hazard*(1.3 if pos=='RB' else 1))&(remaining==0)
   remaining[hit]=rng.choice([1,2,4,8],hit.sum(),p=[.5,.3,.15,.05])
   available[:,week,p]=(remaining==0)&(week+1!=bye)
   remaining=np.maximum(0,remaining-1)
 available[:,:,IDX['Henderson']] &= np.arange(W)[None,:]>=recovery[:,None]
 # Some vacated usage goes to the modeled teammate. This is a hypothetical rule.
 for a,b in [('Montgomery','Marks'),('Marks','Montgomery'),('Harrison','Wilson'),('Wilson','Harrison')]:
  mu[:,:,IDX[b]]*=np.where(available[:,:,IDX[a]],1,1.35)
 # Anchor the remaining Week 1 games to supplied projections in every world.
 mu[:,0,:]=np.array([p[3] for p in DATA])
 # Team environment creates correlated weekly outcomes, including Allen/Kincaid.
 teams={t:rng.lognormal(-.15**2/2,.15,(N,W)) for t in sorted({p[2] for p in DATA})}
 scores=np.zeros_like(mu)
 for p,(_,pos,team,_,_) in enumerate(DATA):
  cv={'QB':.4,'RB':.65,'WR':.75,'TE':.8,'K':.55,'DEF':.9}[pos]
  scores[:,:,p]=mu[:,:,p]*teams[team]*rng.gamma(1/cv**2,cv**2,(N,W))*available[:,:,p]
 # Week 1 projection anchored to screenshot; finished scores cannot change.
 scores[:,0,IDX['Price']]=6.8; scores[:,0,IDX['Rams']]=2
 # No hindsight: lineup selection uses noisy forecast, not realized score.
 forecast=mu*rng.lognormal(-.2**2/2,.2,mu.shape)*available
 totals={}
 for policy,ids in POLICIES.items():
  selected=np.zeros_like(available)
  for pos,count in [('QB',1),('RB',2),('WR',2),('TE',1),('K',1),('DEF',1)]:
   candidates=[p for p in ids if DATA[p][1]==pos]
   order=np.argsort(forecast[:,:,candidates],axis=2)[:,:,-count:]
   for k in range(order.shape[2]):
    chosen=np.array(candidates)[order[:,:,k]]
    np.put_along_axis(selected,chosen[:,:,None],True,axis=2)
  candidates=[p for p in ids if DATA[p][1] in ('RB','WR','TE')]
  f=np.where(selected[:,:,candidates],-1,forecast[:,:,candidates])
  chosen=np.array(candidates)[f.argmax(axis=2)]
  np.put_along_axis(selected,chosen[:,:,None],True,axis=2)
  # Preserve the two completed Week 1 starting slots; Price is forced at RB.
  selected[:,0,IDX['Price']]=True
  rbs=[p for p in ids if DATA[p][1]=='RB' and p!=IDX['Price']]
  # Re-select other Week 1 RB and flex after fixing the completed Price slot.
  selected[:,0,rbs]=False
  wrs=[p for p in ids if DATA[p][1]=='WR']; tes=[p for p in ids if DATA[p][1]=='TE']
  for c,num in [(rbs,1),(wrs,2),(tes,1)]:
   selected[:,0,c]=False
   order=np.argsort(forecast[:,0,c],axis=1)[:,-num:]
   for k in range(num): selected[np.arange(N),0,np.array(c)[order[:,k]]]=True
  c=[p for p in ids if DATA[p][1] in ('RB','WR','TE')]
  f=np.where(selected[:,0,c],-1,forecast[:,0,c])
  selected[np.arange(N),0,np.array(c)[f.argmax(axis=1)]]=True
  totals[policy]=(scores*selected).sum(axis=(1,2))
 result={'world':role+'/'+injury,'pairs':{},'moves':{}}
 for a,b in PAIRS:
  d=scores[:,:,IDX[a]].sum(1)-scores[:,:,IDX[b]].sum(1)
  result['pairs'][a+' over '+b]=round(float((d>0).mean()*100),2)
 for policy,v in totals.items():
  if policy=='Hold':continue
  d=v-totals['Hold']
  result['moves'][policy]={'win_pct':round(float((d>1e-8).mean()*100),2),
    'tie_pct':round(float((abs(d)<=1e-8).mean()*100),2),
    'mean_points':round(float(d.mean()),2),
    'p10':round(float(np.quantile(d,.1)),2),'p90':round(float(np.quantile(d,.9)),2)}
 assert np.isfinite(scores).all() and (scores>=0).all()
 return result

if __name__=='__main__':
 out=[simulate(r,i) for r in ['screenshot','challengers','incumbents'] for i in ['low','medium','high']]
 print(json.dumps({'seasons':N*len(out),'weeks':W,'scenario_results':out},indent=2))
