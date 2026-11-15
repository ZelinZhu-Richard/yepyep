# Challenge r1-1 against consolidation-r0

Fetched evidence: packets/c1-1.jsonl (c1-1-e001 to e007; 5 fetches). Records with c1-1 IDs are new; p-IDs refer to the packets the consolidation already cites.

## Objections, ranked by how much they would change the decision

### 1. Rank 1 (employer-paid time) is right, but the evidence behind it is the wrong evidence, and the strongest measurement was in a fetched source and left out
- The consolidation backs rank 1 with Axess Lab's EUR 15/hour, 10 hours a month scheme (p03-e013) and three PSF Developers-in-Residence (p01r-e018 to e020). That is one small firm's policy and three named people, so the shortlist calls availability "Low".
- The same Register article behind p04r-e009/e010 says company salaries that explicitly include maintenance make up 24% of maintainer income (c1-1-e001). Direct company payments are 5%, foundations 3% and governments 1% (c1-1-e002). By that measure employer salaries are the largest paid source, about 2.6x the direct payments, foundation and government shares combined (24% against 9%).
- Consequences:
  - The availability of rank 1 is understated. Employment is the main way money reaches maintainers, not a niche.
  - "Corporate sponsorship of full-time maintainers" is listed as a gap (section 9) when it is partly measured.
  - The consolidation reads p04r-e010 as "denominator not stated". The article does state it: shares of overall maintainer income (c1-1-e002).
- Caveats: this is a vendor survey (Tidelift) of about 400 self-selected maintainers (c1-1-e003). The figure is a share of income, not of people. Its origin is the same as p04r-e009 to e012, so it is not independent.
- Also: the article gives 47% "unpaid" next to the 60% "unpaid hobbyists" the consolidation quotes (c1-1-e003). Section 4 reports only the 60% figure, which overstates how many are unpaid. The 2021 figure of 46% (p02-e010) is closer to 47%.

### 2. The claim that "no distribution exists" for GitHub Sponsors is too strong, and rank 5 can be bounded
- The source behind p04r-e013 also says Sponsors "supports over 70,000 maintainers and organizations". It also says each organization-funded sponsorship runs nearly 15 times the average individual one (c1-1-e005).
- Over $100M over about 7 years across more than 70,000 recipients gives a mean of roughly $1,400 lifetime per recipient, around $200 a year. With heavy skew the median is lower still.
- This is a crude bound, not a distribution, and the recipients include organizations. It is enough to move rank 5 from "a judgment" to "measured as tiny for the typical recipient". It also fits the HN anecdote of low four figures over seven years (p03-e016).
- The 40% organization share (p04r-e014) combined with the 15x size ratio implies that the money depends on a few corporate sponsors. That concentration risk is not in the tradeoffs.

### 3. Missing route: public funders now employ maintainers directly, and the evidence ignores the intake problem
- The Sovereign Tech Fellowship hires up to 12 maintainers. Employees get EUR 64,000 to 82,000 a year for two years and must be located in Germany; freelancers are paid market hourly rates (c1-1-e006).
- This is the clearest case in the whole evidence of a stated salary paid to individual maintainers. The consolidation cites no salary figure for any route and lists "salary amounts unknown" as a gap.
- Caveat: intake closed on April 6, 2026. That fits a pattern the consolidation notes only for the bug-resilience bounty: STA programmes open and close. The fund (EUR 50,000 minimum, p01r-e012) is the only one shown as always open.
- Rank 3 treats "grants" as one block. It should separate contract work and employment (fellowship, STF maintenance contracts) from one-off grants (the $10,000 Secure OSS Fund award, p01r-e016).

### 4. The funding-impact study is a funder's self-evaluation and is presented as neutral
- The study behind p04r-e015/e016 was run by a data scientist at the Sovereign Tech Agency, on what look like the agency's own maintenance contracts (c1-1-e004). It covers 4 funded projects against 62 unfunded ones.
- Its finding that funding speeds up existing maintainers without adding contributors is plausible. It should be labelled vendor or funder-sourced in section 3, alongside GitHub and Tidelift, and not be the only "effect of funding" evidence besides p04r-e003.

### 5. Open Source Pledge was cut for weak evidence, but full-source evidence is available and it deserves reinstatement
- The consolidation excludes it (section 8) because it was snippet-only (p04r-e022) and had "no compliance evidence".
- The pledge's own site reports $9,200,672 raised, $4M+ of it in the past year, from members paying more than $2,000 a year per employed developer directly to maintainers and foundations (c1-1-e007).
- That is self-reported and unaudited, and the split between maintainers and foundations is not given. It still supports reinstating the pledge as a corporate-giving route at the same evidence level as Sentry (p03-e015) and the Secure OSS Fund. Its origin is close to Sentry's (the pledge was started from Sentry's giving program), so it is not independent of p03-e015.

### 6. Independence and survivorship across the shortlist
- Rank 2 (open core / dual licensing) rests on two self-reported winners: Sidekiq (one blog, p02-e001 to e004) and lightGallery (one post, p02-e006). No base rate or failure case was gathered for solo commercial licensing. The rank "Medium to high" is pure survivorship. Rank it with the same caution as sponsorware, or flag the missing denominator.
- Rank 4 (Tidelift/Sonar) has only vendor sources (p02-e008 to e012). The 2024 survey, also from the vendor, says it is a small share of income. "Medium" reliability has no independent support.
- Rank 9 (bounties) uses one maintainer's decision (curl, p04r-e004 to e008, one origin) plus one critique blog (p03-e004). "Brittle" is plausible but it is n=1 for a program shutting down.

## Excluded or downranked items

- Open Source Pledge: reinstate (objection 5).
- Tea (p03-e011): exclusion is fair. It is a plan, not an operating route.
- Alpha-Omega figures (p01r-e022, e023): excluded for weak evidence, fairly. They were not refetched here.
- Courses and books (rank 7): correctly marked as not project income. Keep as a side route.

## Absent from the evidence entirely

- Consulting, paid support and training contracts by individual maintainers. This is a common route for independents and has zero records.
- Patreon, Ko-fi, Buy Me a Coffee and thanks.dev. Also Polar.sh, which was funding infrastructure and has pivoted; it would be a useful failure case.
- Open Collective's public ledgers. These could give a real per-collective distribution and were not used.
- Foundations employing staff maintainers (Linux Foundation, Rust Foundation, Zig Software Foundation, Ruby Central). Ruby Central's 2025 RubyGems governance and funding dispute is a counterexample to "sponsor-funded role = reliable".
- Academic and science funding: CZI Essential Open Source Software, NumFOCUS small development grants, NSF POSE. Scientific-software maintainers are a large community that is entirely absent.
- Non-US/EU perspectives: payout region limits beyond the Sponsors docs, tax and KYC burdens for maintainers in the Global South.
- The counterargument that paying maintainers changes motivation or governance (crowding out, capture by sponsors), beyond the curl incentive hypothesis.

## Where the consolidation holds up

- The duplicate and origin handling in section 2 is accurate, and the exclusion of the p01 and p04 first passes is respected.
- The bounty conclusion (low, brittle) and the reading of the donation study (p04r-e001 to e003) are faithful to the quotes.
- The caveat that most figures are totals, not per-maintainer income, is correct. My additions narrow that gap but do not close it.
- Treating Sovereign Tech Fund's EUR 50,000 minimum as an eligibility barrier for individuals is correct.
