

import csv
import json

# Read Chart of Accounts
with open("data/chart_of_accounts.csv", "r") as file:
    reader = csv.DictReader(file)
    accounts = list(reader)

valid_accounts = {
    account["account_code"] for account in accounts
}

# Read Manual Adjustments
with open("data/manual_adjustments.json", "r") as file:
    data = json.load(file)

entries = data["entries"]

# Store audit results
audit_results = []

print("MANUAL ADJUSTMENTS AGENT")
print("========================")

for entry in entries:

    total_debit = 0
    total_credit = 0
    missing_accounts = []

    debit_accounts = set()
    credit_accounts = set()

    for line in entry["lines"]:

        account_code = line["account"]

        total_debit += line["debit"]
        total_credit += line["credit"]

        if line["debit"] > 0:
            debit_accounts.add(account_code)

        if line["credit"] > 0:
            credit_accounts.add(account_code)

        if account_code not in valid_accounts:
            missing_accounts.append(account_code)

    difference = round(total_debit - total_credit, 2)

    suspicious_accounts = debit_accounts.intersection(
        credit_accounts
    )

    # Prepare reasons
    reasons = []

    if difference != 0:
        reasons.append(
            f"Debit-credit difference: {difference}"
        )

    if missing_accounts:
        reasons.append(
            f"Missing COA accounts: {missing_accounts}"
        )

    if suspicious_accounts:
        reasons.append(
            f"Same account on debit and credit sides: "
            f"{list(suspicious_accounts)}"
        )

    # Final decision
    if difference != 0:
        status = "REJECT"
    elif missing_accounts or suspicious_accounts:
        status = "QUARANTINE"
    else:
        status = "ACCEPT"
        reasons.append("All validation checks passed")

    # Save result
    result = {
        "entry_id": entry["id"],
        "description": entry["description"],
        "debit": total_debit,
        "credit": total_credit,
        "difference": difference,
        "missing_accounts": str(missing_accounts),
        "suspicious_accounts": str(list(suspicious_accounts)),
        "decision": status,
        "reasons": "; ".join(reasons)
    }

    audit_results.append(result)

    print("\n", entry["id"], "-", status)

# Save CSV audit report
with open("output/audit_report.csv", "w", newline="") as file:

    fieldnames = audit_results[0].keys()

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(audit_results)

print("\nAudit report saved successfully!")
print("Location: output/audit_report.csv")
