# Brief r2: how open source funds maintainers (final challenger)

Basis: consolidation-r1, challenge-r1-1, spotcheck (8/8 pass), packets p01-p04. I made 2 fetches on 2026-11-15, tagged [C2-n]. Neither is yet logged as a packet record. C1-n items are challenger-reported and were not re-fetched by the consolidator.
- [C2-1] sonarsource.com/open-source-maintainers (© 2026): "We pay maintainers income based on a number of factors, including customer usage and strategic importance". The page gives no amounts, no count of maintainers paid and no active-status date.
- [C2-2] joshuakgoldberg.com/blog/2025-finances-in-review (2026-02-12): "Both numbers are unusually high for open source." The 2025 lines include typescript-eslint $22,276, consulting $12,625, GitHub Sponsors $11,786, Mocha $7,019, ESLint $6,800, book royalties $5,553, Tidelift $2,900 and thanks.dev $90. The page's own list and table disagree on two lines.

## Shortlist that survived

Each route is scored as reliability per recipient / availability.

1. **Employer-paid maintenance**: high / moderate. Evidence: p03-e006 (verified, n=1, survivorship-biased) and p04-e001 (survey by Tidelift, which sells maintainer pay; C1-1 gives employer 24% vs donations 25%, with no stated base). Tradeoff: the employer sets the priorities, and you have to get the job first.
2. **Public fellowships (Sovereign Tech)**: high / very low. Evidence: C1-2, with up to 12 fellows in 2026, EUR 64-82K for employees who must be in Germany, and freelancers on 3-12 month contracts. The STF service contracts paid through projects (p03-e008, snippet) are a separate and probably larger route.
3. **Solo-owned paid extension or dual licence**: potentially high / low. Evidence is effectively one origin, Sidekiq (p02-e003 verified; e004/e005 snippets with self-reported revenue). lightGallery adds a self-reported snippet (p02-e009). Requirements: a product businesses will pay for, sole copyright, and the work of selling it.
4. **Sponsorship platforms and sponsorware**: low-to-moderate / highest. Evidence: p01-e001, p01-e007 (verified), p03-e001/e002, p04-e003. In C2-2 a self-described "unusually high" earner made $11,786 a year from GitHub Sponsors directly. His larger lines came through project collectives (typescript-eslint, ESLint, Mocha), which matters because it puts fiscal hosts on the path to individual pay. No median exists anywhere.
5. Consulting and media (p04-e004, p04-e012, p03-e011, and C2-2 consulting plus royalties): real but anecdotal. Not ranked.

The bottom of the list is not disputed: fiscal hosts and foundations hold money but are not a source of it (p01-e002/e003/e005/e006); company pledges have unverified delivery (p01-e004); bounty platforms show no payout data (p03-e009/e010/e012); token rewards are gameable (p03-e004/e005).

## Credible niche findings worth keeping
- Sponsorware converts an existing audience into income. Two firsthand accounts support it (p03-e001, p03-e002).
- Token rewards attract spam: Tea (p03-e004, verified).
- Money does not stop people leaving. Goldberg quit independent work at about $4.4K a month (p04-e003, C2-2), and Geerling made a similar point (p04-e012, snippet).
- Dependency-splitting tools exist but pay trivially. thanks.dev paid Goldberg $90 in 2025 (C2-2, n=1; p01-e009).
- The STF fellowship is the best-documented direct public salary (C1-2).

## Still disputed

**A. Tidelift: drop it, or keep it as "status unverified"?**
- Challenger r1: there is no payout data after the acquisition, the homepage redirects to a security product page, and the evidence is pre-acquisition and comes from the seller (C1-3, p02-e001/e002, p04-e001).
- Against dropping it: C2-1 shows the program is still advertised under Sonar in 2026, and C2-2 shows $2,900 paid to one maintainer in 2025.
- My reading: it still exists and still pays, but the amounts are small and the terms opaque. It should be listed as a minor, operating route, not left unverified. The 19% survey share is still unexplained.

**B. Is employer-paid really number 1?**
- Consolidator: yes, on reliability, because a salary is steady.
- Challenger: the survey puts employers level with donations, and the only case is n=1.
- Both positions stand. The ranking is a judgement on reliability, not something measured.

**C. Do Grafana and Canonical count as evidence of employer capacity?**
- Challenger: firms that make money from open source are exactly the employers that pay maintainers.
- Consolidator: revenue is not the same as paying maintainers, and p02-e011 rests on a weak wiki.
- Unresolved. No record counts maintainers on any company's payroll.

**D. Should solo licensing rank above sponsorship?**
- It ranks above on payout per success (Sidekiq). It ranks far below on how many people can use it.
- The answer depends on which axis the user weights. Report both.

**E. Are foundations a source of income?**
- r1 softened its earlier wording. Foundation-paid roles (such as PSF Developer-in-Residence) are asserted but not evidenced.
- C2-2 suggests money paid out of a project's collective is a real individual income line. This is n=1 and the payment mechanism is not verified.

**Settled since r1:** Goldberg's figure is atypical. The author's own words in C2-2 confirm the challenger's claim.

## Gaps: one follow-up wave, by how much each would change the answer

1. **Grants and fellowships packet.** Cover NLnet/NGI (including the dispute over funding cuts), Alpha-Omega, the GitHub Secure Open Source Fund, foundation developer-in-residence roles, and STF contract recipients, with amounts and counts. This could put a well-evidenced niche route into the top three. It is the user's "niche" criterion, and it is currently empty.
2. **Distribution data.** Find the median GitHub Sponsors income, use the Open Collective public ledgers to measure how much of a collective's money reaches individuals, and get the base for the Tidelift 2024 survey from the PDF. Without this, routes 1 and 4 are ordered on anecdote.
3. **Requirements packet.** Cover country eligibility for GitHub Sponsors and Stripe, sanctions exclusions, and the tax and legal burden on individuals. It also covers Overney et al. (ICSE 2020) on how donations are actually spent. This addresses the user's "requirements" criterion directly. Currently there is nothing on it.
4. **Hybrid models.** Freexian's Debian LTS, Igalia-style cooperatives, selling binaries of GPL software, crypto retroactive and quadratic funding (Gitcoin, Optimism RetroPGF, Drips), and Polar.sh. These are niche but have documented individual payouts.
5. Non-US/EU routes (OSPP, Gitee and others). Lower priority for changing the ranking.

Before the final answer: log C1-1..C1-3 and C2-1..C2-2 as evidence records, or cite them as challenger-reported.
