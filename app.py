import argparse,json
from pathlib import Path
from core import analyze,dot

def main():
    a=argparse.ArgumentParser(); a.add_argument('graph',type=Path); a.add_argument('--dot',type=Path); x=a.parse_args()
    try: g=json.loads(x.graph.read_text()); r=analyze(g); print(json.dumps(r,indent=2));
    except (ValueError,OSError,json.JSONDecodeError) as e: print('Error:',e); raise SystemExit(2)
    if x.dot: x.dot.parent.mkdir(parents=True,exist_ok=True); x.dot.write_text(dot(g))
    if not r['acyclic']: raise SystemExit(1)
if __name__=='__main__': main()
