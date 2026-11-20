import json,os
from urllib.request import*
E=os.getenv("MAKEFUN_ENV_URL","")
V=(0,100,320,330,500,900,0)
J=(-33,-31,-18,-14,14,18,31,33)
G=(-17,-16,-15,-1,1,15,16,17)
R=(-16,-1,1,16);D=(-17,-15,15,17)
X={0:2,7:1,112:8,119:4}
B=[0]*128;S=1;C=0;P=-1;n=0;U=35000
Y=[]
class A(Exception):pass
def a(q,y):
 for d in(-15,-17):
  t=q+d*y
  if not t&136 and B[t]==y:return 1
 for d in J:
  t=q+d
  if not t&136 and B[t]==y*2:return 1
 for d in G:
  t=q+d
  if not t&136 and B[t]==y*6:return 1
 for d in R+D:
  t=q+d
  while not t&136 and not B[t]:t+=d
  if not t&136 and B[t] in(y*5,y*(3 if d in D else 4)):return 1
 return 0
def g():
 m=[]
 for q in range(128):
  if q&136:continue
  p=B[q]
  if p*S<=0:continue
  v=p*S
  if v==1:
   d=16*S
   for e in(d-1,d,d+1):
    t=q+e
    if t&136:continue
    x=B[t]
    if e==d:
     if x:continue
    elif x*S<0 or t==P:pass
    else:continue
    if(t>>4)==7*(S>0):
     m+=[q|t<<7|r<<14 for r in(5,4,3,2)]
    else:m.append(q|t<<7)
   if(q>>4)==(1 if S>0 else 6) and not B[q+d] and not B[q+2*d]:m.append(q|q+2*d<<7)
  else:
   for e in(J,D,R,R+D,G)[v-2]:
    t=q+e
    while not t&136:
     x=B[t]
     if x:
      if x*S<0:m.append(q|t<<7)
      break
     m.append(q|t<<7)
     if v in(2,6):break
     t+=e
   if v==6:
    for k,b,t,f,e in((4,1,6,7,1),(4,2,2,0,-1),(116,4,118,119,1),(116,8,114,112,-1)):
     if q==k and C&b and not any(a(k+j*e,-S)for j in(0,1,2)) and not any(B[s]for s in range(k+e,f,e)):m.append(k|t<<7)
 return m
def h(m):
 global S,C,P
 f=m&127;t=m>>7&127;r=m>>14
 p=B[f];x=B[t];e=-1
 if p==S and(t&7)!=(f&7) and not x:
  e=t-16*S;x=B[e];B[e]=0
 Y.append((m,x,e,C,P))
 B[t]=r*S if r else p;B[f]=0
 if p==6*S:
  if abs(t-f)==2:B[t-1 if t>f else t+1]=4*S;B[t+1 if t>f else t-2]=0
  C&=~(3 if S>0 else 12)
 C&=~(X.get(f,0)|X.get(t,0))
 P=(f+t)//2 if p==S and abs(t-f)==32 else -1
 S=-S
def u():
 global S,C,P
 m,x,e,c,p=Y.pop()
 f=m&127;t=m>>7&127;r=m>>14
 S=-S;v=B[t]
 B[f]=S if r else v
 if e>=0:B[e]=x;B[t]=0
 else:B[t]=x
 if v==6*S and abs(t-f)==2:B[t+1 if t>f else t-2]=4*S;B[t-1 if t>f else t+1]=0
 C=c;P=p
def l():
 return[x for x in g() if(h(x),not a(B.index(-6*S),S),u())[1]]
def c(m):
 t=m>>7&127
 return B[t]*S<0 or m>>14 or(t==P and B[m&127]==S)
def o(m):
 t=m>>7&127;x=B[t]
 return V[abs(x)]*16-V[abs(B[m&127])] if x else 0
def z():
 s=0;w=0;b=0
 for i in range(128):
  if i&136:continue
  p=B[i]
  if not p:continue
  a=abs(p);v=V[a];f=i&7;r=i>>4;d=abs(2*f-7)+abs(2*r-7)
  if a==1:v+=(r if p>0 else 7-r)*6
  else:
   v+=(14-d)*(0,0,3,2,0,1,0)[a]
   if a==3:w+=p>0;b+=p<0
  s+=v if p>0 else -v
 s+=30*((w>1)-(b>1))
 return s*S
def f(x,y,d,p):
 global n
 n+=1
 if n>U:raise A
 k=a(B.index(6*S),-S)
 if d<=0 and not k:
  s=z()
  if s>=y:return y
  if s>x:x=s
  m=[v for v in g() if c(v)]
 else:
  m=l()
  if not m:return -99999+p if k else 0
 m.sort(key=lambda v:-o(v))
 for v in m:
  h(v)
  if d<=0 and a(B.index(-6*S),S):
   u();continue
  s=-f(-y,-x,d-1,p+1);u()
  if s>=y:return y
  if s>x:x=s
 return x
def y():
 global n
 n=0
 m=l()
 m.sort(key=lambda v:-o(v))
 b=m[0]
 for d in range(1,9):
  try:
   x=-10**9;c=b
   for v in m:
    h(v);s=-f(-10**9,-x,d-1,1);u()
    if s>x:x=s;c=v
   b=c
  except A:
   while Y:u()
   break
 return b
def w(f):
 global S,C,P
 z=f.split();B[:]=[0]*128;q=112
 for ch in z[0]:
  if ch=='/':q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   p='pnbrqk'.index(ch.lower())+1;B[q]=p if ch.isupper() else-p;q+=1
 S=1 if z[1]=='w' else-1
 C=sum(1<<'KQkq'.index(c)for c in z[2]if c in'KQkq')
 P=-1 if z[3]=='-' else(ord(z[3][0])-97)+(int(z[3][1])-1)*16
def i(m):
 f=m&127;t=m>>7&127
 return'%c%d%c%d'%(97+(f&7),f//16+1,97+(t&7),t//16+1)+('nbrq'[(m>>14)-2] if m>>14 else '')
def t(p,b):
 for _ in range(2):
  try:
   with urlopen(E+p,json.dumps(b).encode()) as x:return json.load(x)
  except Exception:pass
 raise SystemExit(p)
def d():
 if not E:raise SystemExit('no env')
 while True:
  g=t('/game',{})
  if g.get('status')=='done':break
  while g.get('status')=='your_move':
   k=g['game'];w(g['fen'])
   v=y()
   g=t('/move',{'game':k,'move':i(v)})
if __name__=='__main__':d()
