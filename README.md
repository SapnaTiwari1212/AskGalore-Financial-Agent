# AskGalore Financial Agent

## Project Overview

This project is a prototype of an AI-powered financial adjustments validation agent.

The agent reads manual journal adjustments and the Chart of Accounts (COA), performs validation checks, and generates an audit report.

## Prototype Features

- Reads manual adjustments from JSON.
- Reads Chart of Accounts from CSV.
- Checks whether total debits equal total credits.
- Identifies account codes missing from the COA.
- Detects suspicious entries where the same account appears on both debit and credit sides.
- Classifies entries into ACCEPT, REJECT, or QUARANTINE.
- Generates an audit report in CSV format.
- Includes automated unit tests.

## Project Structure

```text
AskGalore-Financial-Agent/
│
├── data/
│   ├── trial_balance.csv
│   ├── chart_of_accounts.csv
│   ├── manual_adjustments.json
│   ├── prior_period_tb.csv
│   └── fx_rates.csv
│
├── src/
│   ├── main.py
│   └── read_data.py
│
├── tests/
│   ├── __init__.py
│   └── test_agent.py
│
├── output/
│   └── audit_report.csv
│
└── README.md
```

## Technologies Used

- Python
- CSV
- JSON
- Python unittest

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd AskGalore-Financial-Agent
```

### 3. Run the agent

```bash
python src/main.py
```

### 4. Run automated tests

```bash
python -m unittest discover -s tests -v
```

## Decision Rules

| Condition | Decision |
|---|---|
| Debit and credit do not match | REJECT |
| Account code missing from COA | QUARANTINE |
| Same account on debit and credit sides | QUARANTINE |
| All validation checks pass | ACCEPT |

## Prototype Results

The prototype processes 10 journal entries:

- 7 ACCEPT
- 1 REJECT
- 2 QUARANTINE

All 5 automated tests pass.

## Important Design Considerations

- Accounting calculations use deterministic Python logic.
- Original input data is not modified.
- Suspicious entries are sent for human review.
- Missing account mappings are not automatically guessed.
- Each decision includes reasons for auditability.

## Limitations

This prototype focuses only on manual journal adjustment validation. It does not yet generate complete financial statements or perform production-level consolidation, foreign currency translation, or intercompany eliminations.

## Future Scope

- Trial Balance validation.
- Automated COA mapping with human approval.
- Intercompany reconciliation.
- Foreign currency conversion.
- Financial statement generation.
- Complete audit trail and approval workflow.