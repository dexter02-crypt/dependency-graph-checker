from collections import deque

def validate(g):
    if not isinstance(g,dict) or not g: raise ValueError('graph must be nonempty object')
    out={}
    for k,v in g.items():
        if not isinstance(k,str) or not k or not isinstance(v,list) or any(not isinstance(x,str) or not x for x in v): raise ValueError('invalid graph')
        if len(v)!=len(set(v)): raise ValueError('duplicate dependency')
        out[k]=list(v)
    missing=sorted({x for v in out.values() for x in v if x not in out})
    if missing: raise ValueError('missing nodes: '+', '.join(missing))
    return out

def cycle(g):
    g=validate(g); color={k:0 for k in g}; stack=[]
    def dfs(u):
        color[u]=1; stack.append(u)
        for v in sorted(g[u]):
            if color[v]==0:
                found=dfs(v)
                if found:return found
            elif color[v]==1:
                j=stack.index(v); return stack[j:]+[v]
        stack.pop(); color[u]=2
    for u in sorted(g):
        if color[u]==0:
            found=dfs(u)
            if found:return found

def analyze(g):
    g=validate(g); c=cycle(g)
    if c:return {'acyclic':False,'cycle':c,'order':None,'depths':None}
    indeg={k:len(v) for k,v in g.items()}; rev={k:[] for k in g}; depth={k:0 for k in g}
    for n,deps in g.items():
        for d in deps: rev[d].append(n)
    q=deque(sorted(k for k,v in indeg.items() if v==0)); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in sorted(rev[u]):
            depth[v]=max(depth[v],depth[u]+1); indeg[v]-=1
            if indeg[v]==0: q.append(v); q=deque(sorted(q))
    return {'acyclic':True,'cycle':None,'order':order,'depths':depth,'max_depth':max(depth.values())}

def dot(g):
    g=validate(g); esc=lambda s:s.replace('\\','\\\\').replace('"','\\"'); lines=['digraph dependencies {','  rankdir=LR;']
    for n in sorted(g): lines.append(f'  "{esc(n)}";')
    for n in sorted(g):
        for d in sorted(g[n]): lines.append(f'  "{esc(d)}" -> "{esc(n)}";')
    return '\n'.join(lines+['}'])+'\n'
