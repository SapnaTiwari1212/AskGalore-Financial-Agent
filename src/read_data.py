import json

# Read JSON file
with open("data/manual_adjustments.json", "r") as file:
    data = json.load(file)

# Get all journal entries
entries = data["entries"]

print("Period:", data["period"])
print("Currency:", data["functional_currency"])
print("Total Journal Entries:", len(entries))

print("\n----- JOURNAL ENTRY DETAILS -----")

# Check each entry
for entry in entries:

    total_debit = 0
    total_credit = 0

    # Add debit and credit from every line
    for line in entry["lines"]:
        total_debit += line["debit"]
        total_credit += line["credit"]

    difference = round(total_debit - total_credit, 2)

    print("\nEntry ID:", entry["id"])
    print("Description:", entry["description"])
    print("Total Debit:", total_debit)
    print("Total Credit:", total_credit)
    print("Difference:", difference)