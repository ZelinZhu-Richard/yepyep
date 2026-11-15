# Challenge r1-1 against consolidation-r0

Fetches used: 4 of 6 (The Register article behind p04-e001; Sovereign Tech fellowship page behind p01-e008; tidelift.com; the Sonar page it redirects to), plus 1 search on the Tidelift/Sonar status. New observations are tagged [C1-n] so they can be logged.

New observations:
- [C1-1] theregister.com/2024/09/18/open_source_maintainers_underpaid (fetched 2026-11-15): "donations (25 percent ...)", "company salaries that explicitly include open source maintenance (24 percent)", "Tidelift (19 percent)", "Direct payments from companies (five percent)", "open source foundations (three percent)", "governments or other public entities (one percent)". The article does not say what these percentages are a share of. It also reports that 47% "say they're unpaid", against 60% "unpaid hobbyists", a gap Tidelift puts down to survey wording.
- [C1-2] sovereign.tech/programs/fellowship (fetched 2026-11-15): "Following our successful pilot program in 2025". For 2026 the agency "will hire up to twelve Sovereign Tech Fellows". Up to 3 are employees paid "€64,000 to €82,000 per year" on two-year contracts, and these must be located in Germany. The rest are freelancers for 3 to 12 months at a negotiated hourly rate. Applications closed 2026-04-06 and contracts start from 2026-05-26.
- [C1-3] tidelift.com now answers 301 and redirects to sonarsource.com/solutions/security/. That page says nothing about paying maintainers. Search results show Sonar announced it would acquire Tidelift on 2024-12-17, said maintainer partners would see "no disruption", and still keeps a "Tidelift: a Sonar company" page at sonarsource.com/open-source-maintainers (not fetched). I found no source from after the acquisition that states payout volumes or terms.

## Objections, ranked by how much they would change the decision

### 1. Shortlist #4 (Tidelift subscription pooling) is out of date, and the survey used to judge it comes from the same seller. Rank 4 is not supported as written.
- The consolidation never mentions that Sonar bought Tidelift (December 2024). The brand homepage now redirects to a Sonar security product page [C1-3]. The how-to-get-paid guide behind p02-e001 and p02-e002 already returned 404 in the packet. Both records are one snippet from one origin, and both are dated around 2022.
- The rank rests on a CEO goal (p02-e002, made before the acquisition) and on a 2024 survey run by Tidelift itself (p04-e001, p04-e002). Nothing shows that payouts continue at any scale in 2025 or 2026.
- Change: mark Tidelift "status unverified after the acquisition". Move it below sponsorship platforms, or turn it into a gap until the sonarsource.com/open-source-maintainers page and payout terms are fetched.

### 2. Shortlist #1 (employer-paid) rests on one person's account plus a misread survey number. It also contradicts the exclusion of Grafana and Canonical.
- Support is p03-e006 (Daniel Roe at Vercel, a single person who got a famous job) and p04-e001. In the survey, "24%" is not a confirmed share of income: the article gives no base for it [C1-1]. On the same basis, donations (25%) come out level with employer pay. So the survey does not back ranking employers first; at most it shows they are about as common as donations. The 47% vs 60% unpaid discrepancy [C1-1] is not mentioned.
- Section 6 excludes p02-e011 (Grafana) and p02-e012 (Canonical) as "company revenue, no payout to maintainers". But companies that sell commercial products are exactly the employers that pay maintainers' salaries. Either reinstate them as evidence of how much employer funding exists, or say plainly that the employer route has no capacity evidence beyond one person.
- Rank 1 is still plausible on reliability, since a salary is steady. But the consolidation should state that its evidence is n=1 and survivorship-biased: maintainers with an employer sponsor are a selected group.

### 3. Shortlist #3 (public funds) is assessed from stale snippets. The program is no longer a pilot, and the evidence is now strong but shows very small capacity.
- The text says "pilot ... snippet evidence". The live page [C1-2] shows a 2026 cohort of up to 12 fellows, published salaries (€64K to €82K), a requirement that employees be located in Germany, and freelance contracts lasting 3 to 12 months. This is the best-documented direct payment to individuals in the whole evidence set. It also shows the limits: about 12 people per year, a competitive application, and a German location requirement for the employment track.
- The STF's larger investment programme (service contracts with projects, EUR 23 to 25M per p03-e008) gets folded into "fellowship". That misses the main route by which public money reaches maintainers: contracting through the project.
- Change: keep rank 3 for reliability per recipient, but record its tiny capacity and restricted eligibility. It is not a general option.

### 4. Shortlist #2 (commercial licence sold by the maintainer) is effectively one origin.
- Three records, p02-e003, p02-e004 and p02-e005, come from one origin (sidekiq). Two are snippets, one of which is a wiki mirror with 2022 prices, and the revenue figure conflicts with Product Hunt's "million-dollar" description. lightGallery (p02-e009) is a vendor blog relaying a self-reported figure, snippet only. Gurux (p02-e007) and Baserow (p02-e006) are companies, not individual maintainers.
- So "maintainer-owned commercial licensing works" rests on Sidekiq alone. The consolidation names survivorship bias but still ranks the route second. It should separate "solo-owned paid extensions or dual licence" (n of about 1.5) from "VC-funded open core", which pays employees and so belongs under the employer route.

### 5. Whole categories are missing, and several match the user's "niche" criterion better than what was kept.
These routes have no record at all, or appear only as a name in the gaps list. Each has public data on payments to individuals:
- NLnet/NGI grants, which pay individuals directly from EU money in small grants. The 2024 to 2025 dispute over NGI funding cuts is also a reliability signal.
- Paid fellowship and developer-in-residence roles: PSF Developer-in-Residence, Rust Foundation fellowships, Linux Foundation fellowships, OpenSSF and Alpha-Omega funded staff. The consolidation treats foundations as "do not create income", which this contradicts.
- Corporate FOSS funds and grants: GitHub Secure Open Source Fund, FOSS Contributor Fund-style programmes.
- Freexian's paid Debian LTS, which pays individual developers by the hour from company subscriptions. It is a working version of the Tidelift idea.
- Worker cooperatives and consultancies (e.g. Igalia), and consulting or training by the maintainer. Feross lists consulting in p04-e004, but it is never ranked.
- Selling binaries or app-store builds of GPL software (e.g. Krita or Ardour builds).
- Crypto retroactive or quadratic funding (Gitcoin, Optimism RetroPGF, Drips). These are distinct from Tea tokens and have actually paid individuals.
- Polar.sh-style issue funding, and its pivot away from it.

Counterarguments that are absent:
- Peer-reviewed work on donations, such as Overney et al., ICSE 2020, which found donations are mostly spent on things other than paying developers and have a small effect on activity.
- Payout eligibility: which countries GitHub Sponsors and Stripe support, and sanctions exclusions. This bears directly on the user's "requirements" criterion.
- Tax and legal burden on individuals.

Communities that are absent: every firsthand case is a visible US or EU, English-language maintainer. Nothing covers Asia (e.g. China's OSPP or Gitee), India, or Latin America.

### 6. Smaller points
- The ranking criterion mixes "reliability per recipient" with "availability". Sovereign Tech (12 people) ranks above sponsorship (open to anyone). The final answer should report both axes, or say clearly which one it ranks on.
- Bounties at #8: the counterexamples (p04-e006 Turso, p04-e007 curl) are security bug bounties run by projects. The consolidation notes this but still uses them to rank bounty platforms. The demotion should rest only on missing payout data (p03-e009, e010, e012 are launch or promotional material), not on those counterexamples.
- Sponsorship #5 uses p04-e003 (Goldberg) as a typical "well-known" figure. That $4,355 a month mixes several income sources, and the author calls it unusually high. p04-e009, e010 and e011 are snippets drawn from summaries. There is still no median. The conclusion ("small") is probably right, but it is based on anecdotes.

## Where the consolidation holds up
- It correctly merges duplicate origins: the GitHub $100M figure (p01-e010 = p04-e005), the Tea records (p03-e004/e005), STF, and the devon-wiki records (p02-e010/e011).
- It is right that platform totals say nothing about per-maintainer adequacy, and right to rate token rewards as unreliable and gameable.
- It is right that fiscal hosts and Apache hold money but do not create income (p01-e002, e003, e006). The exception is the foundation-employed roles listed in objection 5.
- It is right to treat the p04-e001 breakdown as unverified. [C1-1] confirms the figures exist but leaves their base unclear.
- Its exclusions of Ghost (p02-e010), the Redis fork as a funding method (p04-e008), and EU STF advocacy (p03-e007) were made for evidence reasons, not because the items were unusual. They stand.
- Nothing seems to have been cut only for being unusual. The weakness runs the other way: niche routes with good evidence were never collected (objection 5).
