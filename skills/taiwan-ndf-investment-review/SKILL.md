---
name: taiwan-ndf-investment-review
description: Review startup and growth-company investment proposals from both Taiwan National Development Fund (NDF) and institutional VC/PE perspectives. Use for NDF applications, venture investment memos, funding plans, valuation reviews, pre-money/post-money calculations, EPS and dilution analysis, use-of-funds checks, milestone and benefit projections, listing-readiness reviews, investment committee questions, due diligence, and red-flag analysis. Especially useful when a user asks whether a proposed valuation is supportable, what valuation becomes after investment, what returns or operating benefits the investment can produce, or how far a company is from IPO/OTC listing readiness.
---

# Taiwan NDF Investment Review

Use two lenses in parallel:

1. Taiwan National Development Fund / policy-investment fit.
2. Institutional VC/PE investment-committee discipline.

Do not accept management claims at face value. Build a claim-evidence-calculation chain and show unsupported assumptions explicitly.

## Workflow

1. Identify the review target and date.
2. Collect the investment proposal, financial statements, cap table, historical financing, revenue model, use of funds, execution plan, and exit/listing plan when available.
3. Determine the likely NDF route using `references/ndf-routing.md`.
4. Verify current NDF rules from official sources when eligibility, limits, procedures, or deadlines matter. Prefer `df.gov.tw` and the competent ministry/agency for special investment programs.
5. Normalize all financial facts before judging the proposal.
6. Run valuation, ownership, dilution, EPS, and scenario checks. Use `scripts/investment_math.py` when inputs are sufficient.
7. Review the proposal using `references/review-framework.md`.
8. Produce the investment-committee output using `references/output-template.md`.

## Evidence discipline

Classify every material claim as one of:

- Verified fact: directly supported by source documents or authoritative public data.
- Derived calculation: reproducible from verified facts; show the formula and inputs.
- Management assumption: forward-looking claim supplied by the company.
- External assumption: market multiple, growth benchmark, margin benchmark, or comparable-company input.
- Evidence gap: required information is missing, inconsistent, or not auditable.

For major conclusions, connect:

`claim -> evidence -> calculation -> implication`

Do not hide evidence gaps behind polished prose.

## Financial normalization rules

Before discussing valuation, establish at minimum:

- Paid-in capital.
- Shares issued and fully diluted shares.
- Par value if relevant.
- Latest annual and trailing-period revenue.
- Gross profit and gross margin when applicable.
- Operating income.
- Net income after tax.
- Cash and debt.
- Existing preferred shares, options, warrants, convertible notes, or other dilution.
- Historical funding amount and implied valuation, if any.
- Proposed investment amount and proposed ownership percentage.

Never treat paid-in capital as company valuation.

Never treat share capital divided by par value as fully diluted shares without checking options, preferred instruments, convertibles, and pending issuances.

## Valuation checks

Use more than one method when data permits. Prefer methods that match the company's stage and economics.

Common methods:

- Transaction-implied valuation from proposed investment and ownership.
- Last-round valuation, adjusted for elapsed time and changed fundamentals.
- Revenue multiple or ARR multiple for recurring-revenue businesses.
- EBITDA or earnings multiple for profitable mature businesses.
- Comparable-company or comparable-transaction analysis.
- Venture capital method for high-growth early-stage businesses.
- DCF only when cash-flow assumptions are sufficiently grounded.

Always reconcile:

`post-money valuation = pre-money valuation + new primary investment`

For a simple primary round:

`new investor ownership = investment / post-money valuation`

If a document states any two of investment amount, ownership, pre-money, or post-money, derive the others and flag inconsistencies.

Do not use a premium narrative as evidence. Explain what operating metric, comparable, intellectual property, contract backlog, user traction, margin structure, or strategic asset supports the premium.

## EPS checks

Use net income attributable to common shareholders divided by the appropriate share count.

For historical EPS, prefer weighted-average shares for the period.

For post-investment forward EPS, use the expected diluted share count after the financing and clearly state whether the number is a run-rate estimate or a period-weighted estimate.

If the company is loss-making, do not force EPS into a positive-investment story. Focus on cash runway, unit economics, contribution margin, revenue quality, and path to profitability.

When management provides a target EPS, reverse-engineer the required net income and revenue assumptions.

## Use-of-funds and execution checks

Convert each major spending item into an operating milestone.

For each use-of-funds category identify:

- Amount.
- Timing.
- Owner.
- Deliverable.
- KPI.
- Expected commercial effect.
- Dependency.
- Downside if delayed.

Reject vague mappings such as "marketing -> growth". Require a measurable bridge such as headcount, leads, conversion, contracted revenue, gross margin, product launch, regulatory milestone, or deployment capacity.

## Benefit and return bridge

Build a bridge from investment to business result:

`investment -> capability created -> operating KPI -> revenue/cost effect -> profit effect -> valuation implication`

Separate base, upside, and downside scenarios when forecast uncertainty is material.

For every projected benefit, state the time horizon and the leading indicator that can be checked before the financial result appears.

## IPO / OTC listing readiness

Do not answer listing distance with a single time estimate alone. Review readiness across:

- Corporate governance and board structure.
- Financial reporting quality and audit readiness.
- Revenue scale and profitability/cash-flow profile.
- Internal controls.
- Shareholding and cap-table cleanliness.
- Related-party transactions.
- Legal/IP ownership.
- Customer concentration.
- Recurring versus project revenue quality.
- Management depth and key-person risk.
- Information security and data governance when material.
- Underwriter/accountant/legal-adviser preparation.
- Market story and comparable public companies.

State which gaps are gating items and which can run in parallel.

When Taiwan listing or OTC rules materially affect the answer, verify current TWSE/TPEx requirements from official sources rather than relying on memory.

## NDF-specific review

Read `references/ndf-routing.md` when the user asks about National Development Fund participation.

Distinguish:

- Eligibility/routing.
- Investment-commercial quality.
- Policy/strategic contribution.
- Co-investment structure.
- Governance and exit feasibility.

Do not assume that high policy relevance can compensate for an internally inconsistent cap table, unsupported valuation, or non-executable plan.

Do not assume that conventional VC financial return is the only criterion for an NDF program. Use the objective of the specific program verified at the time of review.

## Investment committee challenge mode

When the user asks for a rigorous review, generate the questions a skeptical committee member would ask.

Prioritize questions that could change the decision:

- What exactly supports the current valuation?
- What has changed since the last financing or latest audited period?
- Why is the proposed ownership percentage economically consistent with the investment amount?
- Which forecast inputs are contracted, evidenced, benchmarked, or purely aspirational?
- What happens if revenue is six or twelve months late?
- How much additional capital is required before breakeven?
- What is the next financing trigger and expected dilution?
- Which founder/key-person/IP/customer dependencies can impair value?
- What evidence exists that the funded capability converts into revenue or margin?
- What must be true for the listing plan to be credible?

## Output style

Lead with the answers the decision maker needs. Use numbers before narrative.

When the user asks the common four-question review, answer in this order:

1. Current valuation, current EPS, and the evidence supporting both.
2. Post-investment valuation, ownership, and dilution.
3. Execution duration, measurable outputs, financial effect, and forward EPS scenarios.
4. Listing/OTC readiness: current stage, gating gaps, and milestones required.

Then provide:

- NDF route fit.
- Key red flags.
- Missing evidence.
- Investment committee questions.
- Specific revisions required in the proposal.

Avoid generic startup advice. Tie every finding to the company data.
