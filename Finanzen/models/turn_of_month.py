"""Turn-of-month-Profil und Open/Close-Analyse (5.11.2026). Daten wie kauftag_analyse.py."""
import json
def loadO(f):
    b=json.load(open(D+f))['bars']; idx=pd.to_datetime(b['t'],unit='s').tz_localize('UTC').tz_convert('Australia/Sydney').tz_localize(None).normalize()
    df=pd.DataFrame({'o':b['o'],'c':b['c']},index=idx); return df[~df.index.duplicated()].sort_index()
def tom_profile(s):
    s=s.dropna(); r=np.log(s).diff().dropna()
    df=pd.DataFrame({'r':r}); df['m']=df.index.to_period('M')
    df['k']=df.groupby('m').cumcount()+1; df['n']=df.groupby('m')['r'].transform('size')
    df['kb']=df['n']-df['k']+1
    # label: first 10 trading days as +k, last 8 as -kb, middle 'mid'
    def lab(row):
        if row.kb<=5: return f"L-{int(row.kb)-1}" if row.kb>1 else "L"
        return int(row.k)
    df['lab']=[ (('L' if kb==1 else f'L-{kb-1}') if kb<=5 else k) for k,kb in zip(df.k,df.kb)]
    g=df.groupby('lab').r.agg(['mean','count','std'])
    g['bp']=g['mean']*1e4; g['t']=g['mean']/(g['std']/np.sqrt(g['count']))
    order=list(range(1,19))+['L-4','L-3','L-2','L-1','L']
    g=g.reindex([o for o in order if o in g.index])
    allm=df.r.mean()*1e4
    return g, allm, df
res={}
for name,s in [('Kombi 88/12 AUD',combo),('ACWI AUD',acwi_a),('S&P 500',spx)]:
    g,allm,df=tom_profile(s); res[name]=g
    print(f'== {name}: Ø alle Tage {allm:.1f} bp')
    print('  '+' '.join(f'{i}:{v:.0f}' for i,v in g.bp.items()))
    tom=df[(df.kb==1)|(df.k<=3)].r; rest=df[~((df.kb==1)|(df.k<=3))].r
    from math import sqrt
    t=(tom.mean()-rest.mean())/np.sqrt(tom.var()/len(tom)+rest.var()/len(rest))
    print(f'  TOM (letzter + erste 3 HT): {tom.mean()*1e4:.1f} bp/Tag vs Rest {rest.mean()*1e4:.1f}  t={t:.2f}; Anteil an Gesamtrendite {tom.sum()/df.r.sum()*100:.0f}% bei {len(tom)/len(df)*100:.0f}% der Tage')
    # mid-month window k 11-16 (≈ 15.–23. Kalender)
    mid=df[(df.k>=11)&(df.kb>5)].r
    print(f'  Monatsmitte (HT 11 bis 5 vor Ende): {mid.mean()*1e4:.1f} bp/Tag')
# open vs close VGS + BGBL-like: overnight vs intraday
v=loadO('mcp-TradingView-mcp-tv-get-ohlcv-1793793197026.txt')
on=np.log(v.o/v.c.shift(1)).dropna(); intra=np.log(v.c/v.o).dropna()
print(f'VGS overnight (Close→Open) {on.mean()*1e4:.1f} bp, intraday (Open→Close) {intra.mean()*1e4:.1f} bp, Tage {len(on)}; overnight positiv {100*(on>0).mean():.0f}%')
# chart: average cumulative path by trading day (first 21 TD), combo/ACWI/SPX
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(12,4.5),dpi=150)
cols={'Kombi 88/12 AUD':'#1f6f8b','ACWI AUD':'#e07a5f','S&P 500':'#6c757d'}
for name,g in res.items():
    x=list(range(len(g))); y=np.cumsum(g['mean'].values)*100
    ax[0].plot(x,y,label=name,color=cols[name],lw=2)
    ax[1].bar(np.array(x)+{'Kombi 88/12 AUD':-0.27,'ACWI AUD':0,'S&P 500':0.27}[name],g.bp.values,width=0.27,color=cols[name],label=name)
for a in ax:
    a.set_xticks(range(len(g))); a.set_xticklabels([str(i) for i in g.index],rotation=90,fontsize=7); a.grid(alpha=.3)
ax[0].set_title('Ø kumulierter Verlauf über den Monat (%)'); ax[1].set_title('Ø Tagesrendite je Handelstag (Basispunkte)')
ax[0].set_xlabel('Handelstag (1–18 ab Monatsanfang, L-4…L = letzte 5)'); ax[1].axhline(0,color='k',lw=.6)
ax[0].legend(fontsize=8)
fig.suptitle('Turn-of-the-month: Kombi 88/12 (VGS+EEM in AUD, 2014–2026), ACWI in AUD (2008–2026), S&P 500 (1995–2026)',fontsize=9)
fig.tight_layout(); fig.savefig('tom_chart.png')
d=(on - intra.reindex(on.index)).dropna()
print(f"t overnight {on.mean()/(on.std()/np.sqrt(len(on))):.2f}, t intraday {intra.mean()/(intra.std()/np.sqrt(len(intra))):.2f}")
for y0,y1 in [(2014,2019),(2020,2026)]:
    o=on[(on.index.year>=y0)&(on.index.year<=y1)]; i=intra[(intra.index.year>=y0)&(intra.index.year<=y1)]
    print(y0,y1,f"overnight {o.mean()*1e4:.1f} bp intraday {i.mean()*1e4:.1f} bp")
