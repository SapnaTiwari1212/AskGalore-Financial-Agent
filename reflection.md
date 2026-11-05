# Project Reflection – AskGalore Financial Agent

## 1. Design Decisions

I chose to build a Manual Adjustments Agent as the working prototype because manual journal entries are an important part of financial reporting and require strong validation.

The prototype uses Python to validate debit-credit equality, check account codes against the Chart of Accounts, and identify suspicious entries.

I used three decisions: ACCEPT, REJECT, and QUARANTINE. This makes the system easier to understand and supports human review.

## 2. Use of AI Tools

I used AI tools to understand the assignment, break down the problem, plan the system architecture, and assist with Python implementation and debugging.

I reviewed and tested the generated logic instead of relying on AI output without verification.

## 3. Why Deterministic Logic?

Financial calculations require accuracy and consistency. Therefore, I used deterministic Python rules for debit-credit validation and account checks.

An LLM can help interpret transaction descriptions and suggest possible account mappings, but it should not independently approve accounting entries or perform critical financial calculations.

## 4. Limitations

The current prototype handles manual journal adjustment validation only.

It does not yet implement complete financial statement generation, foreign currency translation, intercompany eliminations, or ERP API integration.

The suspicious same-account check is only a review signal and does not prove an accounting error.

## 5. Future Improvements

I would improve the system by adding:

- Automated COA mapping with human approval.
- Intercompany transaction reconciliation.
- Foreign currency translation.
- Full financial statement generation.
- Database-backed audit history.
- Role-based access and approval workflows.

## 6. Key Learning

This assignment helped me understand how agentic systems can support financial workflows.

My main learning is that reliable financial automation requires a balance between AI assistance, deterministic accounting rules, human approval, and audit traceability.