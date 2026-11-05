# System Architecture: Agentic ERP Financial Statement Generation

## 1. Introduction

The proposed system is an agentic financial reporting platform that converts ERP financial data into four major financial statements:

1. Balance Sheet
2. Profit and Loss Statement
3. Cash Flow Statement
4. Statement of Changes in Equity (SOCIE)

The system focuses on accuracy, traceability, controlled automation, and human approval.

## 2. High-Level Architecture

The system follows a modular architecture.

```text
ERP Data Sources
       |
       v
Data Ingestion Layer
       |
       v
Data Validation Layer
       |
       v
Chart of Accounts Mapping
       |
       v
Financial Processing Agents
       |
       +----------------------+
       |          |           |
       v          v           v
   Adjustment  Intercompany  FX Translation
     Agent       Agent          Agent
       |          |           |
       +----------+-----------+
                  |
                  v
          Consolidation Engine
                  |
                  v
         Financial Statement Builder
                  |
       +----------+----------+
       |          |          |
       v          v          v
   Balance     P&L       Cash Flow
    Sheet
                  |
                  v
                SOCIE
                  |
                  v
          Audit and Approval Layer
                  |
                  v
             Final Reports
```

## 3. Data Ingestion Layer

The system accepts the following inputs:

- Trial Balance (CSV)
- Chart of Accounts (CSV)
- Manual Adjustments (JSON)
- Prior Period Trial Balance (CSV)
- Foreign Exchange Rates (CSV)

The ingestion layer reads files, checks their structure, validates required fields, and preserves the original source data.

## 4. Data Validation Layer

This layer checks:

- Missing values
- Invalid account codes
- Duplicate records
- Debit and credit differences
- Incorrect data formats

Invalid records are rejected or quarantined for further review.

## 5. Chart of Accounts Mapping

The COA mapping agent maps ERP account codes to standardized financial reporting categories.

For example:

- Assets
- Liabilities
- Equity
- Revenue
- Expenses

Exact and approved mappings can be processed automatically.

Ambiguous mappings require finance-team approval. The system must never silently guess an account classification.

## 6. Manual Adjustments Agent

This is the working prototype developed in this repository.

Its responsibilities include:

- Reading manual journal adjustments.
- Checking debit-credit equality.
- Checking account codes against the COA.
- Detecting suspicious same-account debit and credit entries.
- Assigning ACCEPT, REJECT, or QUARANTINE decisions.
- Generating an audit report with reasons.

### Decision Logic

| Condition | Decision |
|---|---|
| Debit and credit are unequal | REJECT |
| Account is missing from COA | QUARANTINE |
| Same account appears on both sides | QUARANTINE |
| All checks pass | ACCEPT |

Rejected and quarantined entries do not proceed automatically into financial statement generation.

## 7. Intercompany Reconciliation Agent

This agent identifies transactions between related legal entities.

It checks:

- Entity identifiers
- Counterparty identifiers
- Intercompany account balances
- Matching debit and credit amounts
- Currency differences

Unmatched or suspicious transactions are sent for human review before elimination.

## 8. Foreign Currency Translation Agent

The FX agent translates foreign currency balances into the required reporting currency.

It uses approved exchange rates and appropriate rate policies, such as:

- Closing rates for balance sheet items.
- Transaction-date or approved average rates for income and expenses.
- Applicable translation adjustments for equity and consolidation.

The system records the exchange rate, rate date, currency pair, and calculation details for traceability.

## 9. Consolidation Engine

The consolidation engine combines financial information from different entities.

Its responsibilities include:

- Combining entity-level trial balances.
- Applying approved intercompany eliminations.
- Processing consolidation adjustments.
- Handling approved currency translation adjustments.
- Maintaining entity-level and group-level balances.

Every elimination must be linked to its original transactions and approval records.

## 10. Financial Statement Builder

The statement builder generates four financial statements.

### Balance Sheet

Shows assets, liabilities, and equity.

Accounting equation:

Assets = Liabilities + Equity

### Profit and Loss Statement

Shows revenue, expenses, and net profit or loss.

Net Profit = Revenue - Expenses

### Cash Flow Statement

Classifies cash movements into:

- Operating activities
- Investing activities
- Financing activities

### Statement of Changes in Equity (SOCIE)

Shows changes in share capital, retained earnings, reserves, and other equity components during the reporting period.

## 11. Role of AI and LLMs

LLMs can assist with:

- Understanding messy descriptions.
- Suggesting possible COA mappings.
- Explaining unusual transactions.
- Summarizing exceptions for finance reviewers.

LLMs should NOT perform:

- Debit and credit calculations.
- Financial statement arithmetic.
- Currency conversion calculations.
- Automatic approval of accounting adjustments.
- Final accounting decisions without validation.

Deterministic Python rules and controlled accounting logic are used for financial calculations.

## 12. Human-in-the-Loop Approval

Human approval is required for:

- Ambiguous COA mappings.
- Unbalanced or suspicious adjustments.
- Unmatched intercompany transactions.
- Unusual FX differences.
- Prior-period restatements.

The system records who approved or rejected an item, when it happened, and why.

## 13. Audit Trail and Traceability

Every processed record should retain:

- Original source reference.
- Processing timestamp.
- Validation results.
- Agent decision.
- Reason for the decision.
- Human approval details.
- Final reporting reference.

This ensures that financial statement numbers can be traced back to source transactions.

## 14. Reliability and Security

The production system should include:

- Role-based access control.
- Encryption of sensitive financial data.
- Idempotent processing to prevent duplicate postings.
- Versioned COA mappings and FX rates.
- Structured logging and monitoring.
- Period-close controls.
- Backup and recovery procedures.

## 15. Limitations and Future Improvements

The current prototype focuses on manual adjustment validation only.

Future improvements include:

- Automated trial balance validation.
- COA mapping recommendations.
- Intercompany matching and eliminations.
- FX translation.
- Full financial statement generation.
- Approval workflows.
- Database-backed audit history.
- Integration with ERP APIs.

## 16. Conclusion

The proposed architecture combines deterministic accounting controls, specialized agents, and human approval to support reliable ERP-driven financial reporting.

The main design principle is that AI assists with interpretation and exception handling, while financial calculations and final accounting controls remain deterministic, explainable, and auditable.