# Brief r2-1: how open-source maintainers get paid

Sources: consolidation-r1, challenge-r1-1, spot-checks, packets p01r, p02, p03, p04r, c1-1, c2-1 (4 fetches). p01 and p04 not cited. DERIVED = reviewer arithmetic, not reported.

## Shortlist that held up

1. **Employment: an employer salary that covers maintenance, a fund-hired role, or employer-paid time.** This is the most reliable route while the job lasts. It is the largest paid source measured: 24% of maintainer income (c1-1-e001), against 5% from direct company payments, 3% from foundations and 1% from governments (p04r-e010, c1-1-e002). The only stated salary in the evidence is EUR 64,000 to 82,000 a year for two years, for up to 12 people based in Germany, and applications closed in April 2026 (c1-1-e006). The PSF Developers-in-Residence depend on their sponsors renewing (p01r-e018 to e020). Requires an employer or a winning application; renewal risk.
2. **One-off grants.** These pay per award but do not recur. The GitHub Secure Open Source Fund gives $10,000 per project through Sponsors, tied to milestones (p01r-e016, e017). The Sovereign Tech Fund only takes work over EUR 50,000 (p01r-e012).
3. **Solo dual licensing or open core.** This can pay well for the winners: Sidekiq (p02-e001) and lightGallery at over $350K (p02-e006), both self-reported. There is no base rate, so survivorship bias is likely. It requires sole copyright and buyers.
4. **Pooled subscription (Tidelift/Sonar).** Every source is the vendor's own (p02-e008 to e012).
5. **Donation platforms (GitHub Sponsors, Liberapay, Open Collective).** These are open to almost anyone (p01r-e003 lists Sponsors' region limits). They pay little to the typical recipient. Sponsors has moved more than $100M (p04r-e013) to more than 70,000 maintainers and organizations (c1-1-e005) since 2019 (c2-1-e002). DERIVED: about $1,400 per recipient over the program's life, roughly $200 a year. Donations show no strong link to project activity (p04r-e003).

Lower down: sponsorware (p03-e001 against p03-e002, e003), courses and books (side income, not income from the project; p03-e012), bounties (low and brittle: p04r-e004 to e008; p01r-e010, e011), and retroactive or token funding (p03-e007, e009).

## Niche findings worth keeping

- **Sovereign Tech Fellowship.** A public funder employs maintainers directly (c1-1-e006). It is the only salaried public programme found.
- **Bounties fail under AI-generated report floods.** curl paid out more than $100K and then ended its bounty (p04r-e004 to e008, one origin). Sovereign Tech rewarded about 80 of 790 submissions and has closed intake (p01r-e010, e011).
- **Open Source Pledge** reports $9.2M in total, $4M+ of it in the past year (c1-1-e007). It handles no money: companies pay maintainers and/or foundations of their own choosing directly (c2-1-e006). That makes the totals unverifiable and leaves the split between maintainers and foundations unknown.

## Disputed points

1. **Is employment "the main way" money reaches maintainers?**
   - Challenger: yes. 24% of income is far more than any other paid source; DERIVED, about 2.6 times the 9% from direct, foundation and government payments combined (c1-1-e001, e002).
   - Consolidation: only within one vendor survey of about 400 self-selected respondents, in which 47% say they are unpaid (c1-1-e003). The figure measures share of income, not share of people.
   - Unresolved; employment ranks first either way.
2. **Is GitHub Sponsors "measured as tiny"?**
   - Now partly settled. The 15x ratio is verified: "Each organization-funded sponsorship runs nearly 15 times the average individual one" (c2-1-e001). The program's age is now sourced: launched 2019 (c2-1-e002).
   - DERIVED: with organizations supplying 40% of the money (p04r-e014) at 15 times the average size, organization sponsorships would be only about 4% of all sponsorships. Concentration on a few corporate sponsors is therefore an inference from two reported figures, not just a hypothesis.
   - Still disputed: whether the mean describes a typical payee. The 70,000 count includes organizations and may count profiles rather than people paid (c1-1-e005). No median exists, and the article gives none (c2-1-e001).
3. **Is the funding-impact study a funder's self-evaluation?**
   - Largely settled for the challenger: the study was done by "a data scientist at the agency" (c2-1-e003), with "62 unfunded projects" as the comparison group (c2-1-e004). The name of the Sovereign Tech Agency comes from the adjacent paragraph, not the same sentence.
   - Label it funder-run. Its result (commits up about 144%, contributors flat; p04r-e015, e016) rests on 4 projects.
4. **Is the Open Source Pledge independent of Sentry?**
   - The About page lists sentry.io under "Initiator" (c2-1-e005). That supports the challenger's link, though as a logo rather than a sentence.
   - Treat the Pledge and Sentry's giving reports (p03-e015) as one origin group.
5. **Rank 2 (licensing) against rank 3 (grants).**
   - Consolidation ranks licensing higher; challenger calls it survivorship. No base rate either way.

## Gaps where one follow-up wave would most change the answer

1. **A per-recipient payout distribution.** Open Collective's public ledgers or a GitHub Sponsors median would settle dispute 2 and rank 5.
2. **Consulting, paid support and training by individual maintainers.** Zero records; possibly a top-two route for independents.
3. **Foundation-employed maintainers and science funders.** Rust Foundation, Zig, Ruby Central's 2025 dispute, CZI EOSS, NumFOCUS and NSF POSE all have zero records. These would test whether "sponsor-funded role = reliable" holds.
4. **Base rates for commercial licensing,** including failures. This decides dispute 5.
5. **Spot-checks.** c1-1 and c2-1 have not been spot-checked. The p01r fee and eligibility records (p01r-e001 to e008) and the Tidelift 2024 primary report have not been checked either.
