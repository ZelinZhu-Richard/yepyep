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
- Token and retroactive funding is unproven for individuals (p03-e007, p03-e009).
- The Open Source Pledge totals $9.2M (c1-1-e007), but it holds no money itself and Sentry initiated it (c2-1-e005, c2-1-e006), so delivery is unverified.

**Niche findings worth keeping.**
- A public funder hiring maintainers directly: the Sovereign Tech Fellowship pays €64,000–82,000 a year (c1-1-e006), and applications are closed.
- A funder's own study found commits up about 144% with contributors flat, on 4 projects (p04r-e016, p04r-e015, c2-1-e003).

**Coverage note.**
- Agents: 4 Haiku collectors, 3 Sonnet (one consolidator for spot-check, consolidation and revision, plus two packet reruns), 2 fresh Opus challengers.
- Spot-check: 18 records. Every quote was on its page, and none was stitched. Claim support: 11 yes, 7 partial, 0 no. All 7 partials were in first passes, so p01 and p04 failed and were rerun; the reruns were 6 of 6 yes. Challenger records were not spot-checked.
- Not covered: paid support, consulting and training; foundation-employed maintainers (Rust, Zig, NumFOCUS); a median payout for any platform; base rates for commercial licensing.
- Stopped after one pass because this is a demonstration run; the round-2 brief lists those gaps as the follow-up wave.
- No finite scan covers every route.
