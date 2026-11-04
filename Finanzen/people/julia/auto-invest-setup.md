# Julia: Betashares Direct auto-invest setup (as of 4 Nov 2026)

Plan: **88 % BGBL / 12 % BEMG**, monthly, funded by an ANZ recurring transfer. Julia does every step herself. Nobody else places orders or opens accounts for her.

## 1. What exactly she buys

| ASX code | Full name | What it is | Fee p.a. | Share |
|---|---|---|---|---|
| **BGBL** | Betashares Global Shares ETF | ~1,300 large and mid companies in developed markets, excluding Australia | 0.08 % | 88 % |
| **BEMG** | Betashares MSCI Emerging Markets Complex ETF | Emerging markets (Taiwan, China, Korea, India, ...) | 0.35 % | 12 % |

Together this closely matches a global all-world index without an Australia overweight (see [welt-etf-kandidaten.md](../../docs/research/2026-11-03_welt-etf-kandidaten.md)).

## 2. Amounts

| Variant | Monthly total | BGBL (88 %) | BEMG (12 %) |
|---|---|---|---|
| A: ongoing rate only | $300 | **$264** | **$36** |
| B: months 1–10 with the $10k staggered in ($1,000 + $300) | $1,300 | $1,144 | $156 |
| B: from month 11 | $300 | $264 | $36 |

- **First investment:** there is no fixed minimum beyond fractional investing "from as little as $10" (Betashares Direct FAQ, checked 4 Nov 2026). The first investment is simply the first month's amount.
- **Open point:** Betashares does not publish a per-ETF minimum for auto-invest on its official pages. A secondary source (Finder) mentions $50. If the app rejects $36 for BEMG, use **BEMG $50 / BGBL $250** (83/17, close enough) or add BEMG quarterly at $108. Check this in the app when setting up.

## 3. Step by step

1. **Open the account** in the Betashares Direct app or website: Australian tax resident, 18+, Australian residential address, ID (driver licence or passport). Enter her **Tax File Number** during sign-up. Without a TFN, tax is withheld from distributions at the top rate.
2. **Note the Cash Wallet details** shown in the app (BSB and account number in her name). The money for every order comes from this wallet.
3. **ANZ recurring transfer** (ANZ app > Pay/Transfer > set a recurring payment): to the Wallet BSB/account, **$300** (or $1,300 in variant B), monthly, **2 business days before** the auto-invest date. Example: transfer on the 1st, auto-invest on the 3rd. Ideally a day or two after payday.
4. **Create the auto-invest plan**: add BGBL with $264 and BEMG with $36 (or the variant B amounts), frequency monthly, pick the start date. Betashares invests the full amount, fractions included, so no cash is left over.
5. **Distributions**: BGBL pays distributions (about 1.2 % a year). By default they go to the Cash Wallet. Set the standing instruction to **reinvest automatically** (allowed under the Betashares Direct PDS of 9 Sep 2026, section 2.5; the exact menu name in the app is not verified). BEMG does not distribute, so nothing to set there.
6. **First month check**: after the first order date, confirm both ETFs appear in the portfolio and the wallet is close to $0.
7. **Variant B only**: after 10 months, change the recurring transfer and the auto-invest amounts down to $300 / $264 / $36.

## 4. Things to know

- **Market just dropped?** Doesn't change the plan. Monthly buying means she automatically buys more units when prices are low. Nobody can reliably time the bottom.
- **Tax**: reinvested distributions are still taxable in the year they are paid. Betashares sends an annual tax statement (AMMA). Keep it for the tax return.
- **Selling**: possible on any ASX trading day in the app, money arrives in the Cash Wallet after settlement (T+2) and can be withdrawn to ANZ. See the Safety Net page.
- **Pause**: auto-invest can be paused or changed at any time in the app.

Sources: [betashares.com.au/direct/auto-invest](https://www.betashares.com.au/direct/auto-invest), [betashares.com.au/direct/faq](https://www.betashares.com.au/direct/faq), Betashares Direct PDS (9 Sep 2026), all checked 3–4 Nov 2026.
