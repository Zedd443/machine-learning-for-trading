import sys
import pandas as pd
import numpy as np

REQUIRED = ["realized_R", "fees", "setup_valid", "rule_violation"]

def max_drawdown(r):
    equity = r.cumsum(); peak = equity.cummax(); dd = equity - peak
    return float(dd.min()) if len(dd) else 0.0

def longest_losing_streak(r):
    longest = cur = 0
    for x in r:
        if x < 0:
            cur += 1; longest = max(longest, cur)
        else: cur = 0
    return longest

def summarize(df):
    r = pd.to_numeric(df["realized_R"], errors="coerce").dropna()
    wins, losses = r[r > 0], r[r < 0]
    pf = wins.sum() / abs(losses.sum()) if len(losses) and losses.sum() != 0 else np.inf
    adherence = (1 - pd.to_numeric(df["rule_violation"], errors="coerce").fillna(0).clip(0,1).mean()) * 100
    return {
        "Trades": len(r), "Win rate %": round(r.gt(0).mean()*100,2) if len(r) else 0,
        "Avg win R": round(float(wins.mean()),3) if len(wins) else 0,
        "Avg loss R": round(float(losses.mean()),3) if len(losses) else 0,
        "Expectancy R/trade": round(float(r.mean()),3) if len(r) else 0,
        "Profit factor": round(float(pf),3) if np.isfinite(pf) else "inf",
        "Net R": round(float(r.sum()),3), "Max drawdown R": round(max_drawdown(r),3),
        "Longest losing streak": longest_losing_streak(r), "Rule adherence %": round(float(adherence),2)
    }

def grouped(df, col):
    if col not in df.columns: return None
    rows=[]
    for key,g in df.groupby(col, dropna=False):
        r=pd.to_numeric(g["realized_R"],errors="coerce").dropna()
        if len(r): rows.append({col:key,"n":len(r),"net_R":round(r.sum(),2),"expectancy":round(r.mean(),3),"win_rate":round(r.gt(0).mean()*100,1)})
    return pd.DataFrame(rows).sort_values("n",ascending=False) if rows else None

def main(path):
    df=pd.read_csv(path)
    missing=[c for c in REQUIRED if c not in df.columns]
    if missing: raise SystemExit(f"Missing columns: {missing}")
    print("\n=== OVERALL ===")
    for k,v in summarize(df).items(): print(f"{k}: {v}")
    for c in ["setup","symbol","direction","regime_1h","session"]:
        t=grouped(df,c)
        if t is not None:
            print(f"\n=== BY {c.upper()} ==="); print(t.to_string(index=False))

if __name__ == "__main__":
    if len(sys.argv)<2: raise SystemExit("Usage: python journal_analyzer.py path/to/journal.csv")
    main(sys.argv[1])
