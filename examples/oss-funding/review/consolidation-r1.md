# Consolidation r1 (revises r0 using challenge-r1-1.md)

Basis: r0 sections 1-4 and 6-7 stand unless amended below. Spot-check unchanged: 8/8 pass, no packets set aside. Challenger observations C1-1..C1-3 were made by the challenger (fetches of The Register, sovereign.tech, tidelift.com on 2026-11-15); I did not re-fetch them. They are used as stated and flagged as challenger-reported. My own r0 spot-check of p04-e001 had confirmed only the 60% and 400+ respondents.

## A. Objection-by-objection disposition

1. Tidelift out of date / seller-run survey: ACCEPTED. Evidence: p02-e001, p02-e002 (one snippet, one origin, pre-acquisition CEO goal), p04-e001/e002 (Tidelift's own survey), C1-3 (Sonar acquisition announced 2024-12-17, tidelift.com now redirects, no post-acquisition payout data found). Tidelift is moved out of the ranking to "status unverified" (below sponsorship). The sonarsource.com/open-source-maintainers page is a follow-up.
2. Employer-paid rests on n=1 and a misread survey number: ACCEPTED IN PART. Accepted: p03-e006 is a single, survivorship-biased case; C1-1 shows the 24% has no stated base and donations are 25%, so the survey shows comparable prevalence only, not a ranking; the 47% vs 60% unpaid discrepancy is noted (r0 reported only 60%). Rank 1 kept on reliability-per-recipient only (salary is steady), flagged as low-evidence. Rejected: reinstating Grafana/Canonical (p02-e011, p02-e012) as evidence of employer capacity. Reason: they show company revenue, not that it pays maintainers; p02-e011 also rests on the weak wiki. They stay excluded as maintainer-funding evidence but are listed as context that commercial firms can employ maintainers (not measured).
3. Public funds assessed from stale snippets: ACCEPTED. Per C1-2, the Sovereign Tech Fellowship is past pilot: up to 12 fellows in 2026; up to 3 employees at EUR 64,000-82,000/yr on 2-year contracts (must be in Germany); the rest freelancers for 3-12 months. Rank 3 kept on reliability per recipient with explicit limits: tiny capacity, competitive, location-restricted. p03-e008 (EUR 23-25M investment programme, snippet) is recognised as contracting money through projects, a distinct route from the fellowship; kept separate. p01-e008 is superseded by C1-2 for fellowship facts.
4. Commercial licence is effectively one origin: ACCEPTED. p02-e003/e004/e005 are one origin (Sidekiq); e004/e005 are snippets, e005 uses 2022 prices; the ~$10M claim is self-reported and the challenger notes a Product Hunt description of "million-dollar" (not seen by me). lightGallery p02-e009 is a single self-reported vendor blog snippet. Gurux p02-e007 and Baserow p02-e006 are companies, so they belong with employer/company funding, not solo-maintainer licensing. Solo-owned licensing is demoted to "evidence n about 1.5, rank retained on reliability only if a product exists", and is ranked below public funds.
5. Missing categories (NLnet/NGI, foundation fellowships and developers-in-residence, GitHub Secure Open Source Fund, Freexian Debian LTS, worker cooperatives and consulting, binary sales, crypto retroactive/quadratic funding, Polar.sh, Overney et al. ICSE 2020, eligibility by country, tax burden, non-US/EU communities): ACCEPTED AS GAPS, NOT AS EVIDENCE. The objection supplies no records or URLs, so none can be ranked or called supported. All are added to the gaps and follow-ups. One r0 statement is corrected: "foundations do not create income" is too strong, since foundation-employed roles are claimed (unevidenced here); p01-e006 shows Apache pooling only. Consulting is evidenced in p04-e004 (Feross, full), listed as an unranked route.
6. Smaller points:
 a. Two axes mixed: ACCEPTED. Ranking now shows both reliability-per-recipient and availability.
 b. Bounty demotion should not use security bug-bounty counterexamples: ACCEPTED. p04-e006 and p04-e007 are program-run bug bounties; the bounty-platform rank rests only on missing payout data (p03-e009, e010, e012 are promotional). The counterexamples are context.
 c. Goldberg figure as typical: ACCEPTED IN PART. p04-e003 is verified at $4,355/mo and mixes sources; "author calls it unusually high" is the challenger's claim and not confirmed by me. Sponsorship conclusion "small" rests on anecdotes (p04-e003, e009, e010, e011 snippets); no median exists.

## B. Amended contradictions and quality notes
- p04-e001 breakdown per C1-1: donations 25%, employer salaries incl. maintenance 24%, Tidelift 19%, direct company payments 5%, foundations 3%, governments 1%; base unstated. Survey sponsor (Tidelift) has an interest. 47% "unpaid" vs 60% "unpaid hobbyists" (wording).
- Public money share in that survey is 1%, against the Sovereign Tech fellowship's high per-person pay: consistent with small capacity.
- Foundations 3% (C1-1) supports "foundations hold money but rarely pay individuals" for the survey sample.

## C. Revised ranking (two axes)
Reliability per recipient / availability:
1. Employer-paid maintenance: high / moderate (survey 24%, base unclear). Evidence n=1 (p03-e006) plus survey; survivorship-biased.
2. Public fellowships (Sovereign Tech): high (EUR 64-82K for employees) / very low (12 fellows, 2026; Germany for employees; freelance 3-12 months). Evidence: C1-2 (challenger), p03-e008.
3. Solo-owned paid extension or dual licence (Sidekiq, lightGallery): potentially high / low (needs product and sole copyright). Evidence effectively one origin plus one self-reported snippet.
4. Sponsorship platforms (GitHub Sponsors, Liberapay) and sponsorware: low-to-moderate, variable / highest (open to anyone, low fees). p01-e001, e007, p03-e001/e002, p04-e003. Donations at 25% in survey (C1-1) so common but small per person.
5. Consulting and paid media (p04-e004, p04-e012, p03-e011): variable; weak evidence; not hard-ranked.
6. Fiscal hosts and foundation pooling (p01-e002/e003/e005/e006): infrastructure, not income; foundations 3% (C1-1).
7. Company pledges (p01-e004): unverified delivery.
8. Bounty platforms (p03-e009/e010/e012): no payout data.
9. Token rewards (p03-e004/e005): gameable, observed spam.
Unranked, status unverified: Tidelift (p02-e001/e002, C1-3).

## D. Added gaps and bounded follow-up (in addition to r0 section 7-8)
1. Fetch sonarsource.com/open-source-maintainers for Tidelift/Sonar payout terms.
2. One packet on grants and fellowships: NLnet/NGI (including funding-cut dispute), Alpha-Omega, GitHub Secure Open Source Fund, PSF/Rust/Linux Foundation roles, with amounts and recipients.
3. One packet on working hybrid models: Freexian Debian LTS, Igalia/cooperatives, binary-sale GPL projects, crypto retro/quadratic funding (Drips, Optimism RetroPGF, Gitcoin), Polar.sh.
4. Requirements packet: GitHub Sponsors/Stripe country eligibility and sanctions, tax burden; peer-reviewed donation studies (Overney et al. ICSE 2020).
5. Non-US/EU communities (China OSPP/Gitee, India, Latin America).
6. Re-fetch C1-1..C1-3 pages and log them as evidence records before they enter the final answer.

## E. Retained from r0 unchanged
Sections 1 (approach catalogue), 2 (evidence quality), 3 (contradictions), 4 (niche views), 6 (exclusions: Ghost p02-e010, Redis p04-e008, STF advocacy p03-e007, curl figures p04-e007, summary-derived figures p04-e002/e009/e010/e011/e012) of consolidation-r0.md. Challenger confirmed these held up.
