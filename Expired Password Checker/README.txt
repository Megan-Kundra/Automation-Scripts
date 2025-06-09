This Python script checks the password change logs to find which passwords are expired.
Ex. Carol Lee,clee,2025-02-15 --> Carol Lee (clee) — Last changed 114 days ago — ❌ EXPIRED

This script asks the user to enter the file path to their .csv password change history log, and then
it displays the status of all the passwords found, days since they were last changed, and some
overall summary statistics.

This script can be easily customized or scaled to parse folders or to check other information.

The password_date_record.csv file can be used to try this script out.

Developed by Megan Kundra
