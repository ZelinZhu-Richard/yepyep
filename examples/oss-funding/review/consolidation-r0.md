# Consolidation r0 (revised with reruns): how open-source projects fund maintainers

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

Limits: only 3 records per packet were checked, so the others are "passed on a sample". Rerun records carry no requirements or origin fields (empty or None), so tradeoffs below come from the claims, counterevidence and uncertainty fields, and from my reading. Origin groups for p01r are not labelled; I group by source page.

## 1. Funding routes found

### A. Donation and sponsorship platforms (p01r)

**A1. GitHub Sponsors**
- Fees and eligibility: no fee on personal-account sponsorships (p01r-e001); up to 6% on organization-account sponsorships (p01r-e002); recipient must live in a supported region (p01r-e003). All three come from one GitHub docs page. Not sampled.
- Scale: more than $100M cumulative (p04r-e013, verified in spot-check; Help Net Security, a news report of a GitHub figure, total only); organizations supply nearly 40% of funding (p04r-e014, same article, not sampled).
- Duplicate: the same Help Net Security article was independently reported by p04r-e013 and p04r-e014. Not two sources.
- Missing: per-maintainer amounts or distribution. $100M cumulative says nothing about the typical maintainer.

**A2. Liberapay**
- No cut of payments, funds itself by donations (p01r-e006); caps donations per donor per week (p01r-e007); passes on payment processing fees (p01r-e008). One page (liberapay.com/about). Not sampled.

**A3. Open Collective and fiscal hosts**
- Hosts may charge Collectives a fee (p01r-e004, verified); hosts can set it to 0% (p01r-e005). One docs page. Fee level is set by each host.

**A4. Evidence on donation outcomes (p04r)**
- A study of GitHub donations: donations are used in many ways (p04r-e001); in the sample, 40% of donation-receiving projects spent under 25% of what they raised and 15% spent over 75% (p04r-e002); no strong evidence that donations go with higher project activity (p04r-e003). One study via a review page, about 60 projects, selection not checked; the paper was not read.
- Open Source Pledge: expects companies to pay at least $2,000 per year per full-time developer (p04r-e022, snippet only). No evidence of compliance was found.

### B. Funds, grants, fellowships and employed roles (p01r)

- GitHub Secure Open Source Fund: $1.25M across 125 projects (p01r-e015, verified), $10,000 per project (p01r-e016), money goes to maintainers via GitHub Sponsors (p01r-e017). Funder's own announcement. Payment is tied to program milestones. Not stated how a project's money is split among its maintainers.
- Sovereign Tech Agency bug-resilience bounty programs: compensate maintainers for fixing found bugs (p01r-e009, verified); more than 790 submissions (p01r-e010); over 80 accepted and rewarded (p01r-e011). Counterevidence on the page: the platform is not taking new reports during backlog processing. This is a closed intake, so availability is currently nil.
- Sovereign Tech Fund: proposed work must cost more than EUR 50,000 (p01r-e012). That is an eligibility threshold, so it excludes small individual grants.
- NGI Zero Commons Fund (NLnet): 45 projects selected in the seventh call (p01r-e013); 272 projects across seven rounds (p01r-e014). Counts only, no grant sizes.
- PSF Developers-in-Residence: Seth Larson's role is sponsored by Alpha-Omega (p01r-e018), Petr Viktorin's by Bloomberg (p01r-e019), Brett Smith's by Anthropic (p01r-e020). This is salaried work for a few named people. No salary amounts. Roles depend on sponsor renewal.
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
- Vendor or funder sources: Tidelift/Sonar (p02-e008 to e012; the surveys in p04r-e009 to e012 and p02-e010), GitHub's own announcement (p01r-e015 to e017), Drips, Optimism. The Tidelift surveys are vendor-run with a commercial interest; the Register is secondary on the 2024 one and the primary PDF was not read.
- Self-reported figures: Sidekiq, lightGallery, Plausible, Jackson, Axess Lab, curl's own payout and report-quality numbers (p04r-e004, e005), Sovereign Tech submission counts.
- Most figures are totals or project counts. Very few are per-maintainer income.

## 4. Outcomes and failure evidence (p04r)

- curl ended its bug bounty in January 2026. It paid over 100,000 USD for 87 confirmed vulnerabilities (p04r-e004). From 2025 under 5% of reports were confirmed vulnerabilities (p04r-e005). The reason was three combined trends including AI slop (p04r-e006); the Register says it was to remove the incentive for low-quality submissions (p04r-e008; not sampled in the rerun spot-check). The maintainer suspects the prospect of money explains why curl gets more bad reports than peers (p04r-e007, a hypothesis).
- Tidelift 2024 survey: 60% of respondents were unpaid hobbyists, unchanged from the prior year (p04r-e009); direct payments from companies and foundations were a small share of income (p04r-e010; denominator not stated). The 2021 survey: 46% unpaid, 26% earn over $1,000 a year (p04r-e021 snippet; p02-e010).
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
| 1 | Employer-paid time or an employed, sponsor-funded role | High while it lasts (p03-e013; p01r-e018 to e020) | Low: a few named people, or employees with a supportive employer | Depends on sponsor or employer renewal; capped hours; salary amounts unknown |
| 2 | Dual licensing or open core, solo-owned | Medium to high for the few that work (p02-e006; p02-e001) | Low: sole ownership plus buyers | Self-reported, survivorship |
| 3 | Large grants and funds (Sovereign Tech Fund, NGI Zero, Secure OSS Fund, Alpha-Omega) | Medium per award, not recurring | Low to medium: competitive, thresholds (EUR 50,000 minimum for STF, p01r-e012), regional limits | Selective, milestone-tied; $10,000 per project (p01r-e016); project counts only (p01r-e014) |
| 4 | Pooled subscription (Tidelift/Sonar) | Medium, no amounts (p02-e009) | Medium: usage-driven | Small share of maintainer income per the 2024 survey (p04r-e010) |
| 5 | GitHub Sponsors, Liberapay, Open Collective donations | Low to medium for most; high for a few | High: open to anyone, with region limits for Sponsors (p01r-e003) | Over $100M cumulative (p04r-e013) but no distribution; donations small; no strong activity link (p04r-e003) |
| 6 | Sponsorware | Low to medium, volatile | Low: needs audience | p03-e001, e002, e003 |
| 7 | Courses, books, memberships | Medium for individuals | Medium | Not income from the project (p03-e012) |
| 8 | Retroactive or token funding | Low, lumpy | Low | p03-e007, e009; KYC and price risk |
| 9 | Bounties | Low and brittle | Medium | p04r-e004 to e008; p03-e004; closed intake at Sovereign Tech |

Ranking 5 is the one most affected by the missing data: availability is highest but no distribution of what maintainers actually receive was found. Where I put it relative to 3 and 4 is a judgment, not a measurement.

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
- Primary sources for the Tidelift surveys and the four-project study were not read.
- Corporate sponsorship of full-time maintainers, consulting and paid support contracts are not covered as separate routes.
- Only 3 records per rerun packet were checked, including the fee claims (p01r-e001, e002, e003), which were not.

## 10. Bounded follow-ups

1. Spot-check the p01r fee and eligibility records (p01r-e001 to e003, e005 to e008), which drive the platform comparison.
2. Find a distribution of GitHub Sponsors or Open Collective payouts per recipient.
3. Read the Tidelift 2024 primary report to check p04r-e009 and e010.
4. Fetch Alpha-Omega and Sentry reports to turn p01r-e022, e023 and p03-e015 into full-source records.
