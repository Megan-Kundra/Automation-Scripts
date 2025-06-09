import csv
from datetime import datetime

# Constants
EXPIRY_DAYS = 90

# Get CSV file path
file_path = input("Enter the full path to the user password CSV file: ")

# Initialize counters
total_users = 0
expired_users = 0
valid_users = 0

try:
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\nPassword Expiry Report (Threshold: 90 days)\n" + "-" * 45)
        
        for row in reader:
            total_users += 1
            name = row["Name"]
            username = row["Username"]
            last_changed = datetime.strptime(row["LastChanged"], "%Y-%m-%d")
            days_old = (datetime.now() - last_changed).days

            if days_old > EXPIRY_DAYS:
                expired_users += 1
                status = "❌ EXPIRED"
            else:
                valid_users += 1
                status = "✅ VALID"

            print(f"{name} ({username}) — Last changed {days_old} days ago — {status}")

        # Summary
        print("\nSummary Statistics\n" + "-" * 45)
        print(f"Total users checked:     {total_users}")
        print(f"✅ Valid passwords:       {valid_users}")
        print(f"❌ Expired passwords:     {expired_users}")

except FileNotFoundError:
    print(f"⚠️ File not found: {file_path}")
except Exception as e:
    print(f"⚠️ Error: {e}")
