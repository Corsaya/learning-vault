"""Rebuild the packet's scaled PNG diagrams and printable PDF with Matplotlib."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Arc

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 14, 'figure.facecolor': 'white'})
BLUE, ORANGE, RED = '#1769aa', '#c66a00', '#bd2142'
records = []
pdf = PdfPages(OUT.parent / 'AP_Physics_Drawings.pdf')

def arrow(ax, start, delta, color=BLUE, label=None):
    start, delta = np.array(start, dtype=float), np.array(delta, dtype=float)
    ax.annotate('', xy=start+delta, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5, shrinkA=0, shrinkB=0, mutation_scale=16))
    if label:
        ax.annotate(label, start+delta*.5, xytext=(7,7), textcoords='offset points', color=color,
                    fontsize=11, bbox=dict(facecolor='white', edgecolor='none', alpha=.85, pad=1))

def frame(ax, points, unit='units', ticks=True):
    points=np.array(points, dtype=float)
    lo,hi=points.min(axis=0),points.max(axis=0)
    span=max(max(hi-lo),1)
    center=(lo+hi)/2
    ax.set_xlim(center[0]-.7*span,center[0]+.7*span)
    ax.set_ylim(center[1]-.7*span,center[1]+.7*span)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0,color='#9aa4af',lw=.8);ax.axvline(0,color='#9aa4af',lw=.8)
    ax.grid(True,alpha=.18)
    ax.set_xlabel(f'East / +i  ({unit})');ax.set_ylabel(f'North / +j  ({unit})')
    for s in ax.spines.values(): s.set_visible(False)
    if not ticks: ax.set_xticks([]);ax.set_yticks([])

def save(fig, slug, title, section, note=''):
    fig.suptitle(title, fontsize=17, weight='bold', y=.98)
    fig.text(.5,.025,note or 'Equal horizontal and vertical scales. North is up; East is right.',ha='center',fontsize=10)
    fig.tight_layout(rect=(.02,.13,.98,.93))
    fig.savefig(OUT/f'{slug}.png',dpi=180)
    pdf.savefig(fig)
    plt.close(fig)
    records.append((section,title,slug,note))

def polar(m,a): return np.array([m*math.cos(math.radians(a)),m*math.sin(math.radians(a))])
def expr(x,y,unit=''):
    return f'({x:g} i {"+" if y>=0 else "−"} {abs(y):g} j) {unit}'
def result_text(v,unit):
    x,y=v;ang=math.degrees(math.atan2(abs(y),abs(x)))
    return f'R = ({x:.2f} i {y:+.2f} j) {unit}    |R| = {np.linalg.norm(v):.2f} {unit}\n{ang:.1f}° {"N" if y>=0 else "S"} of {"E" if x>=0 else "W"}'

fig,ax=plt.subplots(figsize=(8,7))
vs=[(0,10),(-5,0),(0,-20),(15,0)]
frame(ax,[(0,0)]+vs,'m')
for v,l in zip(vs,['10 m N','5 m W','20 m S','15 m E']): arrow(ax,(0,0),v,label=l)
save(fig,'01-intro-vectors','Drawing vectors: introductory example','Drawing vectors to scale')

pairs=[([(10,0),(-30,0)],['10 mi E','30 mi W'],'mi'), ([(0,6),(0,-12)],['6 m/s N','12 m/s S'],'m/s'),
       (None,[],'gallons'), ([(15,0),(20,0)],['15 N E','20 N E'],'N'), ([(2,0),(0,-10)],['2 mph E','10 mph S'],'mph'),
       ([(0,9),(0,-9)],['9 N N','9 N S'],'N'), ([(-1500,0),(0,-1000)],['1500 m W','1000 m S'],'m'),(None,[],'mph')]
for n,(vs,labels,unit) in enumerate(pairs,1):
    fig,ax=plt.subplots(figsize=(8,7))
    if vs is None:
        ax.axis('off')
        msg='4 gallons and 20 gallons\n\nVolume is scalar.\nNo vector arrows can be drawn.' if n==3 else '7 mph and 28 mph\n\nNo directions are supplied.\nThese are speeds, so vector arrows cannot be drawn.'
        ax.text(.5,.5,msg,ha='center',va='center',transform=ax.transAxes,fontsize=18)
    else:
        starts=[(0,0),(0,3)] if n==4 else [(0,0),(0,0)]
        frame(ax,[(0,0)]+[tuple(np.array(s)+v) for s,v in zip(starts,vs)],unit)
        for s,v,l,c in zip(starts,vs,labels,[BLUE,ORANGE]):arrow(ax,s,v,c,l)
    save(fig,f'02-pair-{n:02}',f'Drawing vectors — problem {n}','Drawing vectors to scale', 'Parallel arrows are offset for visibility; lengths use the same scale.' if n==4 else '')

# Displacements measured visually from rendered pages 6 and 7; arbitrary drawing units.
graphical=[[(0,-92),(119,0)],[(0,76),(-75,-30)],[(-78,-57),(126,-57)],[(141,104),(48,66)],[(104,0),(-208,0)],[(53,-105),(-79,0)],[(-102,-102),(-113,-116)]]
for n,vs in enumerate(graphical,1):
    a,b=np.array(vs,dtype=float)/25
    fig,axs=plt.subplots(1,2,figsize=(11,6))
    if n in [5,7]:
        # Collinear sums: show each arrow in a parallel lane with construction guides.
        unit=a/np.linalg.norm(a); normal=np.array([-unit[1],unit[0]])*.5
        starts=[normal,-normal,a*0]
        for s,v,c,l in zip(starts,[a,b,a+b],[BLUE,ORANGE,RED],['A','B','R']):
            base=s if l!='B' else a+s
            arrow(axs[1],base,v,c,l)
        for p in [(0,0),a,a+b]:
            p=np.array(p);axs[1].plot([p[0]-normal[0],p[0]+normal[0]],[p[1]-normal[1],p[1]+normal[1]],':',color='gray')
    else:
        arrow(axs[1],(0,0),a,BLUE,'A');arrow(axs[1],a,b,ORANGE,'B');arrow(axs[1],(0,0),a+b,RED,'R')
    left_start = np.array([.45,-.45]) if n==7 else np.array([0,0])
    arrow(axs[0],(0,0),a,BLUE,'A');arrow(axs[0],left_start,b,ORANGE,'B')
    for ax in axs:frame(ax,[(0,0),a,b,a+b],'drawing scale',False)
    axs[0].set_title('Given arrows (offset for visibility)' if n==7 else 'Given arrows, moved to a common tail');axs[1].set_title('Head-to-tail addition; R = A + B')
    note='Unlabeled source arrows: approximate scan proportions; no numerical magnitude is given.'
    if n in [5,7]:note+='\nParallel lanes separate overlapping arrows; dotted guides align endpoints.'
    save(fig,f'03-addition-{n:02}',f'Graphical vector addition — problem {n}','Graphical addition',note)

fig,ax=plt.subplots(figsize=(10,8))
for k,(v,l) in enumerate(zip([1,-1,3,5,-3,-5,.5,-.5],['X','−X','3X','5X','−3X','−5X','½X','−½X'])):
    y=7-k;arrow(ax,(0,y),(v,0),BLUE if v>0 else ORANGE)
    ax.text(-5.8,y,l,va='center',fontsize=15)
ax.set_xlim(-6.1,5.8);ax.set_ylim(-.7,7.7);ax.set_aspect('equal');ax.set_xticks(np.arange(-5,6,.5),minor=True)
ax.set_xticks(range(-5,6));ax.set_yticks([]);ax.grid(axis='x',which='both',alpha=.2);ax.axvline(0,color='gray',lw=.8)
ax.set_xlabel('Signed length in multiples of |X| (choose X pointing East)')
save(fig,'04-scalar-multiplication','Scalar multiplication — all eight vectors','Scalar multiplication','Positive multiples keep direction; negative multiples reverse it. All arrows share one scale.')

def component(ax,v,unit):
    x,y=v
    frame(ax,[(0,0),(x,0),(x,y),(0,y)],unit)
    if x:arrow(ax,(0,0),(x,0),BLUE,f'{x:g} i')
    if y:arrow(ax,(x,0),(0,y),ORANGE,f'{y:g} j')
    arrow(ax,(0,0),(x,y),RED,'R')

for n,(v,unit) in enumerate([((-10,5),'m'),((4,6),'mi'),((5,-20),'mi'),((-12,36),'mph'),((-20,-40),'N'),((30,100),'ft')],1):
    fig,ax=plt.subplots(figsize=(8,7));component(ax,v,unit)
    save(fig,f'05-components-{n:02}',f'Vector components — problem {n}\nR = {expr(*v,unit)}','Vector components')

trig=[(4,5),polar(20,50),polar(12,210),(-6,3),polar(15,-80),(-1,-7),(9,-2),polar(5,130),(3,8)]
for n,v in enumerate(trig,1):
    v=np.array(v);fig,ax=plt.subplots(figsize=(8,7));component(ax,np.round(v,2),'units')
    theta=math.degrees(math.atan2(v[1],v[0]));ref=0 if v[0]>=0 else (180 if v[1]>=0 else -180)
    r=np.linalg.norm(v)*.23
    ax.add_patch(Arc((0,0),2*r,2*r,theta1=min(ref,theta),theta2=max(ref,theta),color=RED))
    mid=math.radians((theta+ref)/2)
    ax.text(r*1.25*math.cos(mid),r*1.25*math.sin(mid),f'{abs(theta-ref):.1f}°',fontsize=10)
    note=result_text(v,'units')
    if n==2:note+='\nGiven 40° from vertical = 50° from horizontal.'
    if n==5:note+='\nSource arrow points down and right: the x component is positive.'
    save(fig,f'06-trig-{n:02}',f'Magnitude and trigonometry — problem {n}','Magnitude and trigonometry (supporting drawings)',note)

multi=[([polar(10,90),polar(6,140),polar(15,-20),polar(5,260)],'m',['10 m N','6 m, 40° N of W','15 m, 20° S of E','5 m, 80° S of W']),
       ([polar(15,90),polar(10,210),polar(4,75)],'mi',['15 mi N','10 mi, 30° S of W','4 mi, 75° N of E']),
       ([(100,0),(0,-20),(-45,0),(0,20),polar(35,135),polar(75,-60)],'ft',['100 ft E','20 ft S','45 ft W','20 ft N','35 ft, 45° N of W','75 ft, 60° S of E'])]
for n,(vs,unit,labels) in enumerate(multi,10):
    vs=np.array(vs);vs[abs(vs)<1e-10]=0
    fig,axs=plt.subplots(1,2,figsize=(12,7.5));colors=[BLUE,ORANGE,'#598b32','#7756aa','#008c95','#8c564b']
    for k,(v,c) in enumerate(zip(vs,colors),1):
        arrow(axs[0],(0,0),v,c,str(k))
        axs[0].plot([v[0],v[0],0],[0,v[1],v[1]],'--',lw=.8,color=c,alpha=.6)
    pts=np.vstack(([0,0],np.cumsum(vs,axis=0)))
    for k,(s,v,c) in enumerate(zip(pts,vs,colors),1):arrow(axs[1],s,v,c,str(k))
    arrow(axs[1],(0,0),pts[-1],RED,'R')
    frame(axs[0],np.vstack(([0,0],vs)),unit);frame(axs[1],pts,unit)
    axs[0].set_title('Given vectors and component projections');axs[1].set_title('Head-to-tail sum')
    rows=[f'{k}. {l}: ({v[0]:.2f} i {v[1]:+.2f} j) {unit}' for k,(v,l) in enumerate(zip(vs,labels),1)]
    # Put component values on a separate, generous lower band.
    fig.suptitle(f'Multi-vector sum — problem {n}',fontsize=17,weight='bold')
    fig.tight_layout(rect=(0,.31,1,.94))
    fig.text(.05,.255,'\n'.join(rows),va='top',fontsize=10)
    fig.text(.60,.22,result_text(pts[-1],unit),va='top',fontsize=11,color=RED)
    slug=f'07-multi-vector-{n}'
    fig.savefig(OUT/f'{slug}.png',dpi=180);pdf.savefig(fig);plt.close(fig)
    records.append(('Final multi-vector problems',f'Multi-vector sum — problem {n}',slug,''))

pdf.close()
lines=['# AP Physics Summer Work — Drawings','',
       'Scaled diagrams for every drawing exercise in [[AP Physics Summer Work.pdf]], plus supporting diagrams for trigonometry 1–9 and final sums 11–12.', '',
       '**Print:** [[AP_Physics_Drawings.pdf]] (35 pages). Individual PNG files are in `drawings/`.', '',
       'Numerical arrows use equal horizontal and vertical scales within each diagram. Blue/orange show components; red shows the resultant. Scales can differ between problems. The unlabeled graphical additions use approximate arrow proportions read from PDF pages 6–7, not invented physical magnitudes.', '',
       '**Source correction:** Trig problem 5 points down and right: +2.60i − 14.77j, or 80° South of East. Problem 2 gives 40° from vertical (50° from horizontal). Drawing-pair problems 3 and 8 are scalars and have no vector drawing.', '']
section=None
for s,title,slug,note in records:
    if section!=s:lines += [f'## {s}',''];section=s
    lines += [f'### {title}','',f'![[drawings/{slug}.png]]','']
lines += ['## Rebuilding the images','','Generated with Matplotlib for exact numerical geometry. Run `python drawings/generate_drawings.py` from this folder to regenerate the PNG files and PDF.','']
(OUT.parent/'AP_Physics_Summer_Work_Drawings.md').write_text('\n'.join(lines))
print(f'Wrote {len(records)} PNGs, gallery, and PDF to {OUT.parent}')
