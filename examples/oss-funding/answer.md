# How open-source projects fund their maintainers (lead's answer)

Ranked by how reliably money reaches an individual, with how many people each
route is open to. IDs point to records in `packets/`. "Derived" means a
reviewer computed it; it is not a reported figure.

| Rank | Route | Reliability per person | Open to | Key evidence |
| --- | --- | --- | --- | --- |
| 1 | Employment that covers maintenance: an employer salary, a fund-hired role, employer-paid time | High while the job lasts | Moderate; the public programmes are tiny | c1-1-e001, c1-1-e006, p01r-e018 |
| 2 | One-off grants (GitHub Secure Open Source Fund, Sovereign Tech Fund) | High per award, no recurrence | Low; invitation or application | p01r-e016, p01r-e017, p01r-e012 |
| 3 | Selling a commercial licence or paid edition yourself | High for the few who succeed | Low; needs sole copyright and buyers | p02-e001, p02-e006 |
| 4 | Pooled subscriptions (Tidelift, now Sonar) | Unclear | Packages its customers use | p02-e008 (vendor-sourced only) |
| 5 | Donation platforms (GitHub Sponsors, Liberapay, Open Collective) | Low for a typical recipient | Almost anyone | lead-e001, p04r-e013, c1-1-e005, p04r-e003 |

**The correction the lead made.** Both review rounds called employment "the
largest paid source measured" (24%, c1-1-e001). The source puts donations
slightly higher, at 25% (lead-e001). That figure was only in the failed p04
first pass, so no reviewer saw it. Employment stays first on reliability per
person, not on volume: by share of income in this survey, donations and
salaries are level. The same survey puts 60% of respondents as unpaid
hobbyists (lead-e002). It is a vendor survey of about 400 self-selected
maintainers (c1-1-e003).

**Donations are wide but thin.** GitHub Sponsors has moved more than $100M
(p04r-e013) to over 70,000 maintainers and organizations (c1-1-e005).
Derived: about $1,400 per recipient over the programme's life. No median
exists. Organizations supply nearly 40% of the money (p04r-e014), so a small
number of corporate sponsors carry much of it. Donations show no strong link to
project activity (p04r-e003).

**Weak or failing.**
- Bounties collapsed under AI-generated reports; curl ended its programme (p04r-e004 to p04r-e008, one origin).
- Token rewards backfired: tea paid by packages controlled, about 70% of the npm packages it drew were farming, and it halted rewards (p03r-e009, p03r-e010, p03r-e011).
- Retroactive funding does pay: Optimism's third round reached 501 recipients, median about 45K OP against 300K for the top 1% (p03r-e012, p03r-e013). It pays in tokens, and recipients mix projects and people.
- The Open Source Pledge totals $9.2M (c1-1-e007), but it holds no money itself and Sentry initiated it (c2-1-e005, c2-1-e006), so delivery is unverified.

**Niche findings worth keeping.**
- Retainers: one maintainer funds full-time work with a small set of company retainers and advises pricing them at 25–100% of an engineer's pay (p03r-e022, p03r-e023).
- Sponsorware: one self-reported case grew GitHub Sponsors income to $112,680 a year (p03r-e002, p03r-e004); there is no base rate.
- A public funder hiring maintainers directly: the Sovereign Tech Fellowship pays €64,000–82,000 a year (c1-1-e006), and applications are closed.
- A funder's own study found commits up about 144% with contributors flat, on 4 projects (p04r-e016, p04r-e015, c2-1-e003).

**Coverage note.**
- Agents: 4 Haiku collectors, 4 Sonnet (one consolidator for spot-check, consolidation and revision, plus three packet reruns), 2 fresh Opus challengers.
- Spot-check: 21 records. Every quote was on its page, and none was stitched. Claim support: 13 yes, 8 partial, 0 no, all 8 partials in first passes. p01 and p04 failed at review time and were rerun.
- A late correction: code review of this example found that p03-e013's quote stops before the conditions its claim states. The lead logged the corrected verdict (review/lead-spotcheck.jsonl), so p03 also fails and was rerun as p03r, which passed 3 of 3. The consolidations and challenges were written while p03 still counted. The lead checked each point they took from p03 against p03r: sponsorware, token rewards, retroactive funding, courses and employer-paid time all hold or are restated above with p03r IDs. No p03 record is cited as evidence.
- Challenger and lead records were not spot-checked.
- Not covered: foundation-employed maintainers (Rust, Zig, NumFOCUS); a median payout for any platform; base rates for commercial licensing. Paid support and consulting are covered only by individual accounts (p03r-e019, p03r-e020, p03r-e022).
- Stopped after one pass because this is a demonstration run; the round-2 brief lists those gaps as the follow-up wave.
- No finite scan covers every route.
