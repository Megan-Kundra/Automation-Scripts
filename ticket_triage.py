import csv
import os
from collections import defaultdict

# Define keywords for categories
CATEGORY_KEYWORDS = {
    "Hardware": ["laptop", "printer", "monitor", "keyboard", "mouse", "docking", "screen", "hdmi", "fan"],
    "Software": ["word", "slack", "teams", "email", "outlook", "photoshop", "jira", "app", "software", "crash", "install", "update", "antivirus", "powerpoint", "excel"],
    "Access": ["access", "login", "log in", "vpn", "permission", "account", "password", "reset", "two-factor", "authentication", "admin rights"],
    "Network": ["wifi", "wi-fi", "ethernet", "network", "disconnect", "internet", "drive", "server"],
}

def categorize_ticket(description):
    desc = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in desc for keyword in keywords):
            return category
    return "Other"

# Gets file path from user with error handling 
while True:
    file_path = input("Enter the full path to your tickets CSV file (or 'q' to quit):\n> ").strip()
    if file_path.lower() == "q":
        print("👋 Exiting program.")
        exit(0)
    if os.path.isfile(file_path):
        break
    print(f"❌ File not found at '{file_path}'. Please try again.\n")

# Process the given file
categorized_tickets = []

try:
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = categorize_ticket(row["description"])
            categorized_tickets.append({
                "id": row["id"],
                "description": row["description"],
                "category": category
            })
except Exception as e:
    print(f"❌ Error reading file: {e}")
    exit(1)

# Output summary
summary = defaultdict(int)
for ticket in categorized_tickets:
    summary[ticket["category"]] += 1

print("\n📊 Ticket Summary Report:")
for category, count in summary.items():
    print(f"  - {category}: {count} ticket(s)")

# Save categorized results
output_file = "categorized_tickets.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "description", "category"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(categorized_tickets)

print(f"\n✅ Categorized tickets saved to '{output_file}'")
