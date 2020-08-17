import os
import csv


file_path = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

num_months = 0
totalPNL = 0
changes = 0.0
with open(file_path, "r") as data:
    reader = csv.reader(data, delimiter = ",")
    header = next(reader)
    for row in reader:
        pnl = int(row[1])
        num_months += 1
        if num_months == 1:
            prev = pnl
        else:
            changes += (pnl - prev)
            prev = pnl
        totalPNL += int(row[1])
avgChange = changes / (num_months - 1)

print(f"Total Months: {num_months}")
print(f"Total: ${pnl}")
print(f"Average Change: $ {avgChange}")

