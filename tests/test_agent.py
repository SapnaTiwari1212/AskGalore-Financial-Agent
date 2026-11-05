
import csv
import subprocess
import sys
import unittest
from pathlib import Path


class TestManualAdjustmentsAgent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Run the agent before testing
        subprocess.run(
            [sys.executable, "src/main.py"],
            check=True,
            capture_output=True,
            text=True
        )

        # Read generated audit report
        with open("output/audit_report.csv", "r") as file:
            reader = csv.DictReader(file)
            cls.results = list(reader)

    def test_total_entries(self):
        self.assertEqual(len(self.results), 10)

    def test_unbalanced_entry_rejected(self):
        entry = next(
            row for row in self.results
            if row["entry_id"] == "JE-002"
        )
        self.assertEqual(entry["decision"], "REJECT")

    def test_missing_account_quarantined(self):
        entry = next(
            row for row in self.results
            if row["entry_id"] == "JE-005"
        )
        self.assertEqual(entry["decision"], "QUARANTINE")

    def test_suspicious_entry_quarantined(self):
        entry = next(
            row for row in self.results
            if row["entry_id"] == "JE-008"
        )
        self.assertEqual(entry["decision"], "QUARANTINE")

    def test_decision_counts(self):
        decisions = [
            row["decision"] for row in self.results
        ]

        self.assertEqual(decisions.count("ACCEPT"), 7)
        self.assertEqual(decisions.count("REJECT"), 1)
        self.assertEqual(decisions.count("QUARANTINE"), 2)


if __name__ == "__main__":
    unittest.main()
