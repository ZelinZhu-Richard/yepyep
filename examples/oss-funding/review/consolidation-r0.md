# Consolidation r0: how open-source projects fund maintainers

Scope: 46 records, 4 packets (p01 platforms/foundations, p02 commercial, p03 niche, p04 failures). Spot-check: 8 of 8 pass, no failed packets, so nothing set aside. Passes were on 2 random full_source records per packet; 4 of the 8 had a quote stitched from separate sentences (substance present). Spot-check covers 8 of 29 full_source records only. Raw URLs are in the packets.

## 1. Approaches by category (evidence IDs, duplicates/origins)

A. Donations and sponsorship (individual-facing)
- GitHub Sponsors: p01-e001 (docs, full), p01-e010 (scale, snippet), p04-e005 (scale, full). Duplicate origin: the $100M figure in p01-e010 and p04-e005 is the same GitHub-announced number reported by Help Net Security; count once. It is self-reported by the platform.
- Liberapay: p01-e007 (full, verified). Zero platform cut, processor fees apply.
- Patreon/Tidelift/Sponsors mix experiments: p04-e004 (Feross, full).
- thanks.dev (dependency-tree splitting): p01-e009 (snippet, The Register).
- Open Source Pledge (company pays $2,000/FTE/yr): p01-e004 (full). It is a pledge; it does not handle funds, so delivery is unverified.

B. Fiscal hosts and foundations (money goes to the project, not necessarily a person)
- Open Collective / Open Source Collective: p01-e002, p01-e003 (both full; same origin, Open Collective docs). Host fee 10% at OSC; platform takes 15% of host fees.
- NumFOCUS: p01-e005 (full, verified); fiscal sponsorship plus small development grants. Apache: p01-e006 (full): general fund pooling, so it does not pay individuals by default (tension with maintainer-pay goal).

C. Commercial models (maintainer or company earns from the software)
- Open core / paid extensions: Sidekiq p02-e003 (full, verified), p02-e004 and p02-e005 (snippets; same origin group sidekiq; ~$10M/yr, ~2,000 customers are the maintainer's own podcast claim; price list dated 2022); Baserow p02-e006 (full, company blog).
- Dual licensing: Gurux p02-e007 (full), MySQL p02-e008 (snippet, wiki), lightGallery $350K/4 yrs p02-e009 (snippet, vendor blog, self-reported, one developer).
- Hosted SaaS: Ghost p02-e010 (snippet; cited wiki, weak), Grafana $1B ARR p02-e011 (snippet, same wiki source as e010; company-scale, not maintainer pay).
- Paid support subscriptions: Canonical p02-e012 (full, verified; $235M subscription vs $56M services). Company-level revenue.
- Subscription pooled to maintainers (Tidelift): p02-e001, p02-e002 (both snippet, same blog page; the "at least half" payout is a CEO goal, not measured).

D. Niche or newer
- Sponsorware: p03-e001 (Porzio, full), p03-e002 (pawamoy Insiders, full). Firsthand, single-maintainer accounts.
- Fair Source / delayed open source: p03-e003 (Sentry, full). A licensing model; payout to maintainers not shown.
- Token/registry rewards (Tea): p03-e004 (verified, Sonatype), p03-e005 (Register; labelled firsthand but is a news article quoting a co-founder). Same origin; evidence is of abuse, not income.
- Employer-paid maintenance: p03-e006 (verified; Daniel Roe at Vercel). Also compare Tidelift survey (p04-e001).
- Public funds: Sovereign Tech Fund p01-e008 (snippet), p03-e007 (advocacy, full), p03-e008 (snippet). Same origin cluster (STF). Fellowship is a pilot that pays maintainers directly.
- Bounty platforms: Algora p03-e009 (HN launch, snippet), Opire/fees p03-e010 (snippet; 5% vs 10% from a dev.to comparison), MergeFund p03-e012 (snippet, launch listing). All launch/promo material, no payout data.
- Paid books/courses: p03-e011 (Haverbeke, snippet; vague "quite a bit"). Geerling p04-e012 (books+YouTube+donations).

## 2. Evidence quality
- full_source 29, snippet_only 17. Snippet-only records mark many figures as search-result summaries, not verbatim page text (p04-e002, e007, e009, e010, e011, e012 explicitly). Treat those as leads.
- Self-reported figures: GitHub $100M (platform), Sidekiq ~$10M and $60K tier (maintainer/FAQ), lightGallery $350K, Grafana $1B ARR, Tidelift payout goal, Goldberg $4,355/mo (verified, individual), DeVault $500/mo vs $6,000 goal (snippet).
- p04-e001 claim includes breakdown figures (donations about a quarter, employer 24%, Tidelift 19%) that the stored quote does not cover; spot-check confirmed only 60% unpaid and 400+ respondents. Treat the breakdown as unverified; Tidelift also sells maintainer pay, so its survey has an interest.
- Origin issues: p02-e010 and p02-e011 both rest on one low-grade research wiki. p01-e010 duplicates p04-e005.
- Several records label news articles as firsthand_report (e.g. p03-e005). Not misrepresentation of content, but the label overstates independence.

## 3. Contradictions and tensions
- Platform totals vs adequacy: $100M+ through Sponsors (p01-e010, p04-e005) against per-project reality ESLint about $17K/yr (p04-e009, snippet), Lemmy about 2,000 EUR/mo (p04-e010, snippet), Feross (p04-e004). Not contradictory once spread across hundreds of thousands of sponsors, but the total says nothing about per-maintainer income.
- Commercial success vs maintainers: Sidekiq/Grafana/Canonical revenue is large, but it accrues to the company or a single founder-seller, not typical maintainers. Survivorship bias.
- Tidelift: positive payout framing (p02-e001/e002) vs survey where Tidelift is about 19% of income (p04-e001, breakdown unverified) and 60% remain unpaid.
- Bounties: promoted (p03-e009/e010/e012) vs retired for AI-slop (p04-e006 Turso full; p04-e007 curl, snippet title-only, figures unverified). Note curl and Turso were bug-report bounties, not feature bounties on bounty platforms; relevance is indirect.
- Money does not equal retention: Geerling (p04-e012) says income does not prevent burnout while earning half of a salary; Goldberg (p04-e003, verified) quit independence despite $4,355/mo.
- Fair Source (p03-e003) vs Redis fork loss (p04-e008): license restriction carries community cost (9 of 24 sampled contributors, small sample).

## 4. Supported niche views
- Sponsorware works as a funding mechanism for individual maintainers who have an audience (p03-e001, e002): supported by two firsthand accounts, no aggregate data.
- Token-reward schemes are gameable (p03-e004/e005): well supported.
- Employer-paid maintenance is a common route to being paid (p03-e006, p04-e001 loosely): supported.
- Paid books/courses/media can add income (p03-e011, p04-e012): weakly supported, anecdotal.
- Public funds (STF) pay maintainers directly: p01-e008/p03-e008 snippet only; the pilot status and scale unverified.

## 5. Ranked shortlist: how reliably money reaches individual maintainers
1. Employer-paid maintenance (p03-e006, p04-e001): regular salary; requires employer interest, may shift priorities; availability limited, and the 24% survey share is unverified.
2. Commercial license/extension sold by the maintainer (Sidekiq p02-e003/e004/e005; dual licensing p02-e007/e009): can be large, goes directly to the owner; needs a product companies pay for, a sole-copyright owner, and sales effort. Figures self-reported, survivorship bias.
3. Public/government programs (STF fellowship p01-e008, p03-e008): direct pay, but pilot, selective, small number of recipients; snippet evidence.
4. Subscription pooling (Tidelift p02-e001/e002): steady if the package is accepted, but requires adopting maintenance commitments; payout share unverified; survey suggests small share of total.
5. Sponsorship platforms (GitHub Sponsors, Liberapay; p01-e001, e007, p04-e005): easy and low fee, but income typically small (p04-e003 about $4.4K/mo for a well-known individual; p04-e009/e010/e011 lower). Sponsorware (p03-e001/e002) improves conversion for those with audience.
6. Fiscal hosts and foundations (p01-e002, e003, e005, e006): reliable for holding and disbursing funds, but they do not create income; Apache pools it.
7. Company pledges (p01-e004): potentially meaningful, but voluntary and the pledge does not handle funds; no delivery data.
8. Bounties (p03-e009/e010/e012): sporadic, one-off; evidence promo-only; counterexamples of retired programs.
9. Token rewards (p03-e004/e005): not a reliable source; observed spam.

## 6. Excluded candidates
- p02-e011 (Grafana ARR) and p02-e012 (Canonical) as maintainer funding: company revenue, no evidence of payout to external maintainers; retained as context.
- p02-e010 (Ghost): secondary wiki only; unreliable.
- p04-e008 (Redis fork): not a funding method; used only for the license-change tradeoff.
- p04-e007 (curl) figures: snippet title only; do not cite figures.
- p04-e002, e009, e010, e011, e012 figures: summary-derived; cite as leads only.
- p03-e007: advocacy for an EU fund, not evidence of payment.

## 7. Remaining gaps
- No data on aggregate share of maintainers by funding route beyond the Tidelift survey (unverified breakdown).
- Sponsorship income distribution (median) missing.
- No fetched evidence on Thanks.dev, Open Source Pledge, STF payouts, Algora/Opire actual payouts.
- Untested: Patreon, Ko-fi, Buy Me a Coffee, crowdfunding, university/research grants (NSF, NLnet, Chan Zuckerberg), corporate programs (GitHub Secure Open Source Fund), foundation salaries (Linux Foundation, Python Software Foundation), bug-bounty-as-income (HackerOne), consulting, paid-for-Patreon-style "feature funding", cryptocurrency/Gitcoin quadratic funding. Ledger niche list included grants and government funds; grants beyond STF not covered.
- Non-English / non-US routes missing.
- Ledger lists p01-p04 as "planned" status; not updated here (outside review/).

## 8. Bounded follow-up
1. Fetch full pages for the 17 snippet-only records, prioritising p01-e008, p02-e001/e002, p04-e002/e007/e009/e010/e011.
2. Pull the Tidelift 2024 report PDF to confirm income breakdown (p04-e001) and Tidelift payout figures.
3. One packet on grants (NLnet, STF, GitHub Secure Open Source Fund, Alpha-Omega) with amounts and recipients.
4. One packet on distribution data (GitHub Sponsors median earnings, Open Collective public ledger).
5. Add 2 more spot-check records per packet when evidence is revised.
