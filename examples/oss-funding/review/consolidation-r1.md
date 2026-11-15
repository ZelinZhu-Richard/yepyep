# Consolidation r1: how open-source projects fund maintainers

Revised from r0 after challenge round 1 (review/challenge-r1-1.md, records c1-1-e001 to e007). Section 11 lists every objection with its disposition. Figures I or the challenger computed are marked DERIVED. I also re-fetched the Register 2024 Tidelift article myself; it shows 47% unpaid, 60% unpaid hobbyists, 24% from salaries that explicitly include maintenance, and 5% / 3% / 1% from direct company payments / foundations / governments (my own page check, not a packet record).

Goal: map funding routes, including niche ones, and say which actually put money in individual maintainers' hands, how reliably, and with what requirements.

## 0. Packets used and spot-check status

Spot-check file: review/spotcheck-1.jsonl (3 random full_source records per packet).

| Packet | Status | Notes |
|---|---|---|
| p01 (first pass) | FAILED, not cited | 3 of 3 checked records were "partial". |
| p04 (first pass) | FAILED, not cited | 2 of 3 "partial". |
| p01r (rerun, donation platforms, funds, grants) | passed | 3 pass / 3 yes (p01r-e009, e015, e004). |
| p02 (commercial) | passed | 1 of 3 partial (p02-e008). |
| p03 (niche) | passed | 1 of 3 partial (p03-e002). |
| p04r (rerun, outcomes and failures) | passed | 3 pass / 3 yes (p04r-e019, e020, e013). |
| c1-1 (challenger records) | not spot-checked | Used with care. c1-1-e001 is flagged by its own author as a quote the tool split; c1-1-e005's quote supports only the 70,000 figure, not the 15x ratio. |

Limits: only 3 records per packet were checked, so the others are "passed on a sample". Rerun records carry no requirements or origin fields (empty or None), so tradeoffs below come from the claims, counterevidence and uncertainty fields, and from my reading. Origin groups for p01r are not labelled; I group by source page.

## 1. Funding routes found

### A. Donation and sponsorship platforms (p01r)

**A1. GitHub Sponsors**
- Fees and eligibility: no fee on personal-account sponsorships (p01r-e001); up to 6% on organization-account sponsorships (p01r-e002); recipient must live in a supported region (p01r-e003). All three come from one GitHub docs page. Not sampled.
- Scale: more than $100M cumulative (p04r-e013, verified in spot-check; Help Net Security, a news report of a GitHub figure, total only); organizations supply nearly 40% of funding (p04r-e014, same article, not sampled).
- Duplicate: the same Help Net Security article was independently reported by p04r-e013 and p04r-e014. Not two sources.
- GitHub says the program supports over 70,000 maintainers and organizations (c1-1-e005; recipients include organizations, and 'supports' may count profiles, not payees). The record also says organization sponsorships average about 15 times individual ones, but its quote does not contain that ratio, so I treat the 15x as unverified.
- DERIVED: $100M divided by 70,000 is roughly $1,400 per recipient over the program's life. This is crude arithmetic, not a reported figure: the divisor may not equal payees, the years the program has run are not in any record, and the mean hides skew. It indicates the typical recipient gets little; it is not a measured distribution. It is consistent with, but not independent corroboration of, the snippet-only anecdote p03-e016.
- Concentration risk is a hypothesis only: organizations supply nearly 40% (p04r-e014), and if organization sponsorships are much larger (unverified 15x, c1-1-e005) a few corporate sponsors could matter a lot.
- Still missing: a real per-recipient distribution.

**A2. Liberapay**
- No cut of payments, funds itself by donations (p01r-e006); caps donations per donor per week (p01r-e007); passes on payment processing fees (p01r-e008). One page (liberapay.com/about). Not sampled.

**A3. Open Collective and fiscal hosts**
- Hosts may charge Collectives a fee (p01r-e004, verified); hosts can set it to 0% (p01r-e005). One docs page. Fee level is set by each host.

**A4. Evidence on donation outcomes (p04r)**
- A study of GitHub donations: donations are used in many ways (p04r-e001); in the sample, 40% of donation-receiving projects spent under 25% of what they raised and 15% spent over 75% (p04r-e002); no strong evidence that donations go with higher project activity (p04r-e003). One study via a review page, about 60 projects, selection not checked; the paper was not read.
- Open Source Pledge: expects companies to pay at least $2,000 per year per full-time developer (p04r-e022, snippet only). No evidence of compliance was found.

### B. Funds, grants, fellowships and employed roles (p01r, c1-1)

Separate two kinds here: employment or contract work (B-i) and one-off grants (B-ii). r0 lumped them.

**B-i. Employment and contracts**
- Sovereign Tech Fellowship: up to twelve maintainers hired, employees at EUR 64,000 to 82,000 per year for a full-time position, two years, Germany-based; freelancers at hourly rates (c1-1-e006, firsthand, programme page). Application period ended April 6, 2026; renewal unknown. This is the only stated salary in the evidence.
- PSF Developers-in-Residence: Larson (Alpha-Omega, p01r-e018), Viktorin (Bloomberg, p01r-e019), Smith (Anthropic, p01r-e020). Salaries not stated; renewal-dependent.
- Company salaries that explicitly include maintenance: 24% of maintainer income in Tidelift's 2024 survey, the largest paid source in it (c1-1-e001; Register report of a vendor survey, about 400 self-selected respondents (c1-1-e003); share of income, not share of people). Direct company payments 5%, foundations 3%, governments 1% (my page check; c1-1-e002 records that these are 'very little of overall maintainer income'). DERIVED: 24% against 9% is about 2.6 times; this is arithmetic on a survey, not a reported ratio.
- Same origin as p04r-e009 to e012; not independent.

**B-ii. Grants and funds**

- GitHub Secure Open Source Fund: $1.25M across 125 projects (p01r-e015, verified), $10,000 per project (p01r-e016), money goes to maintainers via GitHub Sponsors (p01r-e017). Funder's own announcement. Payment is tied to program milestones. Not stated how a project's money is split among its maintainers.
- Sovereign Tech Agency bug-resilience bounty programs: compensate maintainers for fixing found bugs (p01r-e009, verified); more than 790 submissions (p01r-e010); over 80 accepted and rewarded (p01r-e011). Counterevidence on the page: the platform is not taking new reports during backlog processing. This is a closed intake, so availability is currently nil.
- Sovereign Tech Fund: proposed work must cost more than EUR 50,000 (p01r-e012). That is an eligibility threshold, so it excludes small individual grants.
- NGI Zero Commons Fund (NLnet): 45 projects selected in the seventh call (p01r-e013); 272 projects across seven rounds (p01r-e014). Counts only, no grant sizes.
- Open Source Pledge: self-reported $9,200,672 raised, $4M+ in the past year, from members paying more than $2,000 per year per employed developer (c1-1-e007; full source, own site, unaudited, no year for the total, split between maintainers and foundations not given). Reinstated from r0's exclusion (the earlier snippet p04r-e022 gives the same $2,000 expectation). I did not find a record for the challenger's statement that it grew out of Sentry's giving, so I do not assert it.
- Linux Foundation: $12.5M in grants managed by Alpha-Omega and OpenSSF (p01r-e021); does not say what share goes to individuals. Snippet only: Alpha-Omega reports over 70 grants totalling over $20M (p01r-e022) and nearly $4.5M of grants in 2024 (p01r-e023). These two are unverified, and the figures do not obviously agree in scope.

### C. Commercial models (p02)

**C1. Open core / paid extension (Sidekiq)**: p02-e001 (2013 Pro sales $85,000, self-reported), p02-e003 and e004 (2015 tiers: Pro $950/yr, Enterprise priced by thread count), p02-e002 (license split advice), p02-e005 (snippet: later revenue $2M or about $10M, conflicting). e001 to e004 are one maintainer's blog. One standout case; the later figures are unaudited.

**C2. Dual licensing**: p02-e006 (lightGallery, over $350K in four years, self-reported; the page names no licences, the GPL/AGPL detail was from a search summary), p02-e007 (Ghostscript/Artifex; revenue to a company, none found). Needs sole copyright and buyers who want to avoid copyleft.

**C3. Hosted SaaS of an open core**: p02-e013 (Plausible, $1M ARR in 2022; snippet only, cited page returned 404; company-reported).

**C4. Pooled subscription (Tidelift, now Sonar)**: p02-e008 (press release on the acquisition; spot-check partial, since the page is an announcement of a planned acquisition and has no year in the dateline), p02-e009 (pay depends on usage and strategic importance; no amounts), p02-e011 and e012 (snippets: usage-weighted split; 2018 goal of at least half of revenue to maintainers). All from the vendor.

### D. Niche and newer models (p03)

- Sponsorware: p03-e001 (Porzio: income rose at the threshold) against p03-e002 and e003 (Capawesome: quality could not be kept after public release; funding fell after each goal). p03-e002 spot-check partial: dropping funding goals is on the page but not in the quote.
- Bounties: p03-e004 (one critique: bots open draft PRs on Algora bounties), p03-e005 (Opire, promotional, about 5% fee unsourced), p03-e006 (snippet: 27% of a 30-bounty scan stranded). Also the Sovereign Tech programs above (p01r-e009 to e011) and curl's ended bounty (section 4).
- Retroactive and token funding: p03-e007 (Optimism round 2: 71 badgeholders, 10M OP, totals only), p03-e008 (snippet: KYC, 90-day stream), p03-e009 (Radworks via Drips: $1M over a year to 30 dependencies, half token), p03-e010 (snippet: FUNDING.json), p03-e011 (Tea: planned only).
- Employer-paid time: p03-e013 (Axess Lab, EUR 15 per hour, up to 10 hours a month, outside work hours).
- Courses, books, memberships: p03-e012 (Justin Jackson; income from products, not from the project).
- Fair source and company giving: p03-e014 (FSL two-year delay; opinion; no funding data), p03-e015 (Sentry annual giving reports; snippet only, amounts not seen).
- Donation anecdote: p03-e016 (snippet; lifetime donations low four figures over seven years).

## 2. Duplicates and origins

- Help Net Security 2026-07-21: p04r-e013 and p04r-e014 (same article).
- curl bounty ending: p04r-e004 to e007 (Stenberg's blog) and p04r-e008 (The Register, reporting the same decision). One event, two outlets, not independent.
- Tidelift survey: p04r-e009 and e010 (Register), p04r-e011 and e012 (Tidelift's dev.to post), p04r-e021 (snippet of the 2021 survey, same data as p02-e010 if that record is relied on). p02-e010 is also a Tidelift survey.
- Relicensing and forks: p04r-e017 to e019, one Register article.
- GitHub Secure Open Source Fund: p01r-e015 to e017, one GitHub blog post.
- Sidekiq p02-e001 to e004; Capawesome p03-e002 and e003; Drips p03-e009 and e010; Optimism p03-e007 and e008.

## 3. Evidence quality

- Snippet-only (not relied on for rankings): p01r-e022, e023; p04r-e021, e022; p02-e005, e011, e012, e013; p03-e006, e008, e010, e015, e016.
- Funder-run or possibly funder-run: the four-project funding study (p04r-e015, e016) is a thin base of four projects and twelve repositories (c1-1-e004). The challenger says an agency data scientist ran it, but that record's own uncertainty field says the article does not state outright that the funded projects were the agency's. Treat as 'possibly funder-run'; the '62 unfunded projects' detail has no record and is not used.
- Vendor or funder sources: Tidelift/Sonar (p02-e008 to e012; the surveys in p04r-e009 to e012 and p02-e010), GitHub's own announcement (p01r-e015 to e017), Drips, Optimism. The Tidelift surveys are vendor-run with a commercial interest; the Register is secondary on the 2024 one and the primary PDF was not read.
- Self-reported figures: Sidekiq, lightGallery, Plausible, Jackson, Axess Lab, curl's own payout and report-quality numbers (p04r-e004, e005), Sovereign Tech submission counts.
- Most figures are totals or project counts. Very few are per-maintainer income.

## 4. Outcomes and failure evidence (p04r)

- curl ended its bug bounty in January 2026. It paid over 100,000 USD for 87 confirmed vulnerabilities (p04r-e004). From 2025 under 5% of reports were confirmed vulnerabilities (p04r-e005). The reason was three combined trends including AI slop (p04r-e006); the Register says it was to remove the incentive for low-quality submissions (p04r-e008; not sampled in the rerun spot-check). The maintainer suspects the prospect of money explains why curl gets more bad reports than peers (p04r-e007, a hypothesis).
- Tidelift 2024 survey: 60% of respondents were unpaid hobbyists, unchanged from the prior year (p04r-e009), while 47% said they are unpaid for their work (c1-1-e003; my page check). These measure different things, so 'unpaid' is not 60%. Direct company payments, foundations and governments were a small share of overall maintainer income, 5%, 3% and 1% (p04r-e010; c1-1-e002; my page check), so the denominator is overall maintainer income, not stated in r0. Company salaries that include maintenance were 24% (c1-1-e001). Vendor survey, about 400 self-selected respondents. The 2021 survey: 46% unpaid (close to the 47% of 2024), 26% earn over $1,000 a year (p04r-e021 snippet; p02-e010).
- Burnout: 58% had quit (22%) or considered quitting (36%) (p04r-e011); 44% report burnout (p04r-e012). Survey year inferred, publisher's own summary.
- Funding effects: a four-project study found commits up (about 144%) but contributor counts and release frequency flat (p04r-e015, p04r-e016). Very thin base. Donation study: no strong link between donations and activity (p04r-e003).
- Relicensing: Elasticsearch, Terraform and Redis changes each produced a fork (p04r-e017); non-employee contributions to Redis dwindled (p04r-e018); Elasticsearch relicensing cost little because over 90% of contributors were employees (p04r-e019, verified). This shows contribution loss, not maintainer pay.
- Value capture: "create massive amounts of value and capture almost none of it" is one commentator's opinion (p04r-e020, verified).

## 5. Contradictions and tensions

- Bounties: curl paid over $100K (p04r-e004) and then ended the programme as the flood of reports grew (p04r-e005 to e008). Sovereign Tech's bounty paid on 80 of 790 submissions (p01r-e010, e011), about 10%, and is closed to new reports. Bounties pay for narrow work and do not scale as maintainer income; Opire's pitch (p03-e005) is promotional.
- Sponsorware: p03-e001 against p03-e003.
- Sidekiq price and revenue conflicts (p02-e004, p02-e005).
- GitHub Sponsors has moved over $100M (p04r-e013) against no per-maintainer figures, while the Tidelift surveys (p04r-e009, e010) suggest most maintainers are unpaid. The two are not contradictory: a large total can still be spread thinly.
- Donations: a donation study found no strong link to activity (p04r-e003); donations spent little by many projects (p04r-e002).
- Counts: Alpha-Omega "over $20M" and "nearly $4.5M" (p01r-e022, e023) are different scopes from snippets; do not combine.

## 6. Supported niche views

- Sponsorware can work for a maintainer with an audience and can also fail (p03-e001 against p03-e002, e003).
- Fair source, token and retroactive funding show no per-maintainer money in this evidence (p03-e007, e009, e014).
- Employed or sponsored roles (PSF Developers-in-Residence) put money into named individuals but depend on sponsors renewing (p01r-e018 to e020).
- Bounties compensate fixing work in narrow programmes but are brittle under AI-driven report floods (p04r-e004 to e008).

## 7. Ranked shortlist: money reaching individual maintainers

Reliability is whether money reaches a person repeatedly; availability is how many maintainers can use it. Both are judgments from thin evidence; none comes from per-maintainer data.

| Rank | Route | Reliability | Availability | Tradeoffs and key evidence |
|---|---|---|---|---|
| 1 | Employment: employer salary that includes maintenance, employer-paid time, or a fund-hired role | High while it lasts (p03-e013; p01r-e018 to e020; c1-1-e006 at EUR 64,000 to 82,000) | Medium for the general route (24% of surveyed income, c1-1-e001; self-selected vendor survey), very low for each specific programme (Fellowship up to 12 places, closed April 2026, c1-1-e006; Axess capped at 10 hours a month) | Depends on employer or sponsor renewal; Germany-based for the Fellowship; not open to maintainers without an employer or a successful application |
| 2 | Dual licensing or open core, solo-owned | Medium for the winners only; no base rate, so reliability across maintainers is unknown (p02-e006; p02-e001) | Low: sole ownership plus buyers | Two self-reported winners from single posts; survivorship; no failure cases gathered |
| 3 | One-off grants and funds (Sovereign Tech Fund, NGI Zero, Secure OSS Fund, Alpha-Omega); employment and contracts are ranked in row 1 | Medium per award, not recurring | Low to medium: competitive, thresholds (EUR 50,000 minimum for STF, p01r-e012), regional limits | Selective, milestone-tied; $10,000 per project (p01r-e016); project counts only (p01r-e014) |
| 4 | Pooled subscription (Tidelift/Sonar) | Medium at best; all sources are the vendor's, and the vendor's own survey says direct company payments are a small share (p02-e009; c1-1-e002) | Medium: usage-driven | Small share of maintainer income per the 2024 survey (p04r-e010) |
| 5 | GitHub Sponsors, Liberapay, Open Collective donations | Low for the typical recipient (DERIVED mean about $1,400 lifetime, crude; see section 1), high for a few | High: open to anyone, with region limits for Sponsors (p01r-e003) | Over $100M cumulative (p04r-e013) across over 70,000 recipients (c1-1-e005); no real distribution; donations small; no strong activity link (p04r-e003) |
| 6 | Sponsorware | Low to medium, volatile | Low: needs audience | p03-e001, e002, e003 |
| 7 | Courses, books, memberships | Medium for individuals | Medium | Not income from the project (p03-e012) |
| 8 | Corporate giving pledges (Open Source Pledge, Sentry reports) | Unknown; self-reported totals, split with foundations not given (c1-1-e007; p03-e015 snippet) | Unknown | Company-controlled, unaudited |
| 9 | Retroactive or token funding | Low, lumpy | Low | p03-e007, e009; KYC and price risk |
| 10 | Bounties | Low and brittle | Medium | curl (p04r-e004 to e008, one origin), Sovereign Tech's roughly 10% acceptance (p01r-e010, e011) and closed intake, a critique (p03-e004), a stranded-bounty scan (p03-e006, snippet). More than one case, but few and thin |

Ranking 5 is the one most affected by the missing data: availability is highest and the derived mean is low, but no real distribution was found. Where I put it relative to 3 and 4 is a judgment, not a measurement. Row 1 now mixes a general route (employment) with specific programmes; read availability per cell.

## 8. Excluded candidates and records

- The first-pass p01 and p04 records are not cited (packets failed).
- Snippet-only records are used only as pointers (section 3).
- p03-e011 (Tea): planned, not operating.
- p04r-e022 (Open Source Pledge): snippet, and no compliance evidence.
- p01r-e022 and e023: snippet and mismatched scopes.

## 9. Gaps

- No per-maintainer income distribution under any route; GitHub Sponsors and Open Collective do not provide one in these records.
- No payout totals for Tidelift or Sentry; no salary amounts for the Developers-in-Residence.
- Grant sizes for NGI Zero and Alpha-Omega are not sourced to fetched pages.
- Salary amounts exist only for the Sovereign Tech Fellowship (c1-1-e006), now closed.
- Primary sources for the Tidelift surveys and the four-project study were not read.
- Employment is partly measured now (24% of surveyed income, c1-1-e001), but one vendor survey is the only source and its sample is self-selected.
- Not covered at all, with zero records: consulting, paid support and training by individual maintainers; Patreon, Ko-fi, Buy Me a Coffee, thanks.dev and Polar.sh (a possible failure case); Open Collective public ledgers; foundations employing staff maintainers (Linux Foundation, Rust Foundation, Zig Software Foundation, Ruby Central, whose dispute the challenger raised without a record); scientific funders (CZI Essential Open Source Software, NumFOCUS grants, NSF POSE); region, tax and KYC burdens beyond the Sponsors docs; and whether paying maintainers changes motivation or governance. These are listed as gaps, not routes, because no evidence was gathered.
- Only 3 records per rerun packet were checked, including the fee claims (p01r-e001, e002, e003), which were not.

## 10. Bounded follow-ups

0. Spot-check c1-1-e001, e005 and e006 (the records carrying the largest r1 changes) before relying on them.
1. Spot-check the p01r fee and eligibility records (p01r-e001 to e003, e005 to e008), which drive the platform comparison.
2. Find a distribution of GitHub Sponsors or Open Collective payouts per recipient.
3. Read the Tidelift 2024 primary report to check p04r-e009 and e010.
4. Fetch Alpha-Omega and Sentry reports to turn p01r-e022, e023 and p03-e015 into full-source records.

## 11. Disposition of challenge round 1 objections

1. Employment is the main measured paid source; rank-1 availability understated; denominator stated; 47% vs 60% unpaid.
   - ACCEPTED in part. Employment now headed row 1 with availability 'medium' for the route and 'very low' per programme (c1-1-e001, e006). The denominator correction and the 47%/60% correction are applied (c1-1-e002, e003, my page check). The 'corporate sponsorship of full-time maintainers' gap is narrowed.
   - REJECTED: the challenger's reading that employment is simply 'the main way money reaches maintainers'. Support: it is 24% of income in one self-selected vendor survey of about 400 (c1-1-e001, c1-1-e003), and 47% say they are unpaid (c1-1-e003). The 2.6x ratio is DERIVED and kept labelled as such. c1-1-e001 was flagged by its own author as a quote the tool split; I confirmed the 24% sentence on the page myself.
2. GitHub Sponsors distribution is bounded; rank 5 is 'measured as tiny'.
   - ACCEPTED in part: the 70,000 figure (c1-1-e005) and a derived mean (labelled DERIVED, crude); 'no distribution exists' reworded to 'no real distribution'.
   - REJECTED: 'measured as tiny'. The divisor may not be payees, the years of operation are in no record, and recipients include organizations (c1-1-e005 uncertainty). The 15x ratio is not in the record's quote, so the concentration argument is a hypothesis only. p03-e016 is snippet-only and is not corroboration.
3. Sovereign Tech Fellowship and the employment-versus-grant split.
   - ACCEPTED (c1-1-e006). Section 1 B-i/B-ii separated; only stated salary recorded; closed intake noted.
   - Note: the challenger's remark about 'STF maintenance contracts' has no record, so it is not added as a route.
4. The funding-impact study is a funder's self-evaluation.
   - ACCEPTED in part: labelled 'possibly funder-run', thin base noted (c1-1-e004, p04r-e015, p04r-e016).
   - REJECTED as stated: the agency authorship and '62 unfunded' detail. The record's own uncertainty says the article does not say the funded projects were the agency's, and no record has the 62.
5. Reinstate Open Source Pledge.
   - ACCEPTED (c1-1-e007; p04r-e022). Added as a corporate-giving route, unaudited.
   - REJECTED: asserting its origin in Sentry's giving program; no record supports it.
6. Survivorship and independence across ranks 2, 4, 9.
   - ACCEPTED for rank 2 (p02-e001 to e004, p02-e006: two winners, no base rate) and rank 4 (vendor-only, p02-e008 to e012; the vendor's survey, c1-1-e002).
   - REJECTED in part for rank 9: it is not n=1. Besides curl (p04r-e004 to e008, one origin), the Sovereign Tech bounties accepted about 80 of 790 and are closed to new reports (p01r-e010, e011, e009) and there are a critique and a snippet scan (p03-e004, e006). Rank text now lists these and says the evidence is few and thin.
7. Exclusions: Tea (p03-e011) and Alpha-Omega (p01r-e022, e023) stay excluded, as the challenger agreed; courses and books stay a side route (p03-e012).
8. Absent evidence list: ACCEPTED as gaps in section 9, not as routes (no records).
