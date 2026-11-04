"""Kauftag-im-Monat-Analyse (4.11.2026).
Daten: TradingView-Tagesschlusskurse (NASDAQ:ACWI, FX:AUDUSD, SP:SPX, ASX:VGS, AMEX:EEM), lokal als JSON-Export
abgelegt (nicht im Repo, siehe Finanzen/data/). Pfad D anpassen. Ergebnisse: docs/research/2026-11-04_kauftag-analyse.md
"""
import json, pandas as pd, numpy as np
D='Finanzen/data/tradingview/'  # JSON-Exporte, lokal
def load(f):
    b=json.load(open(D+f))['bars']
    s=pd.Series(b['c'],index=pd.to_datetime(b['t'],unit='s').tz_localize('UTC').tz_convert('Australia/Sydney').tz_localize(None).normalize())
    return s[~s.index.duplicated()].sort_index()
acwi=load('mcp-TradingView-mcp-tv-get-ohlcv-1793793145449.txt')
aud=load('mcp-TradingView-mcp-tv-get-ohlcv-1793793151650.txt')
spx=load('mcp-TradingView-mcp-tv-get-ohlcv-1793793152116.txt')
vgs=load('mcp-TradingView-mcp-tv-get-ohlcv-1793793197026.txt')
eem=load('mcp-TradingView-mcp-tv-get-ohlcv-1793793197429.txt')
def inaud(x): a=aud.reindex(x.index,method='ffill'); return (x/a).dropna()
eem_a=inaud(eem); acwi_a=inaud(acwi)
# combo: 88 VGS + 12 EEM(AUD), daily rebalanced, on ASX calendar (EEM AUD ffilled)
e=eem_a.reindex(vgs.index,method='ffill')
r=0.88*vgs.pct_change()+0.12*e.pct_change()
combo=(1+r.fillna(0)).cumprod().iloc[1:]
def table(s):
    s=s.dropna(); months=pd.period_range(s.index[0].to_period('M')+1,s.index[-1].to_period('M')-1,freq='M')
    rows=[]
    for m in months:
        sm=s[s.index.to_period('M')==m]
        if len(sm)<10: continue
        row={}
        for d in range(1,29):
            sub=sm[sm.index.day>=d]; row[d]=(sub.iloc[0] if len(sub) else sm.iloc[-1])
        rows.append(row)
    P=pd.DataFrame(rows)           # buy price per month x day
    rel=P.div(P.mean(axis=1),axis=0) # relative to month's avg across days
    adv=(1/rel-1)*100               # % more units vs avg day
    return adv, len(P)
def report(name,s):
    adv,n=table(s); m=adv.mean(); se=adv.std()/np.sqrt(n)
    a=s.dropna().index[0].date(); b=s.dropna().index[-1].date()
    print(f'== {name} ({a}–{b}, {n} Monate) mehr Anteile vs. Durchschnittstag, %')
    print('  '+' '.join(f'{d}:{m[d]:+.2f}' for d in m.index))
    w=adv[list(range(18,24))].mean(axis=1); o=adv[[1,2,3]].mean(axis=1)
    diff=w-o
    print(f'  bester Tag {m.idxmax()} {m.max():+.2f}, schlechtester {m.idxmin()} {m.min():+.2f}; Tag 19 {m[19]:+.2f} (SE {se[19]:.2f})')
    print(f'  Fenster 18.–23. minus 1.–3.: {diff.mean():+.2f} % (t={diff.mean()/(diff.std()/np.sqrt(n)):.2f}); 18.–23. besser in {100*(diff>0).mean():.0f} % der Monate')
    h=n//2
    for lab,sl in [('1. Hälfte',slice(0,h)),('2. Hälfte',slice(h,n))]:
        mm=adv.iloc[sl].mean(); print(f'    {lab}: bester {mm.idxmax()} {mm.max():+.2f}, schlechtester {mm.idxmin()} {mm.min():+.2f}, 18–23 {mm[18:23].mean():+.2f}, 1–3 {mm[1:3].mean():+.2f}')
    return m

def detr(s):
    s=s.dropna(); t=(s.index-s.index[0]).days.values
    lp=np.log(s.values); b=np.polyfit(t,lp,1)[0]
    return pd.Series(np.exp(lp-b*t),index=s.index), b*365
for name,s in [('Kombi 88/12 AUD',combo),('ACWI AUD',acwi_a),('S&P 500',spx)]:
    d,mu=detr(s); adv,n=table(d); m=adv.mean()
    w=adv[list(range(18,24))].mean(axis=1); o=adv[[1,2,3]].mean(axis=1); diff=w-o
    print(f'{name}: Drift {mu*100:.1f}%/J | trendbereinigt: bester {m.idxmax()} {m.max():+.2f}, schlechtester {m.idxmin()} {m.min():+.2f}, Tag19 {m[19]:+.2f}, 18–23 vs 1–3 {diff.mean():+.2f} (t={diff.mean()/(diff.std()/np.sqrt(n)):.2f})')
    print('   '+' '.join(f'{k}:{v:+.2f}' for k,v in m.items() if k in (1,3,5,8,10,12,15,17,19,21,23,25,27)))

out={}
for name,s in [('Kombi 88 VGS / 12 EM, AUD',combo),('VGS (≈BGBL), AUD',vgs),('EM (EEM) in AUD',eem_a),('ACWI in AUD',acwi_a),('S&P 500 USD',spx)]:
    out[name]=report(name,s)
pd.DataFrame(out).round(3).to_csv('dom_results.csv')
