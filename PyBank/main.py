import os
import csv


file_path = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

num_months = 0
pnl = 0
with open(file_path, "r") as data:
    reader = csv.reader(data, delimiter = ",")
    header = next(reader)
    for row in reader:
        num_months += 1
        pnl += int(row[1])


print(f"Total Months: {num_months}")
print(f"Total: ${pnl}")

