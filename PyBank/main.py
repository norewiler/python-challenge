import os
import csv


file_path = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

num_months = 0
totalPNL = 0
totalChanges = 0.0
greatInc = 0
greatDec = 0
with open(file_path, "r") as data:
    reader = csv.reader(data, delimiter = ",")
    header = next(reader)
    for row in reader:
        pnl = int(row[1])
        num_months += 1
        if num_months == 1:
            prev = pnl
        else:
            change = pnl - prev
            totalChanges += (change)
            if change > greatInc:
                greatInc = change
                greatIncMonth = row[0]
            elif change <greatDec:
                greatDec = change
                greatDecMonth = row[0]
            prev = pnl
        totalPNL += int(row[1])
avgChange = totalChanges / (num_months - 1)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${totalPNL}")
print(f"Average Change: ${round(avgChange, 2)}")
print(f"Greates Increase in Profits: {greatIncMonth} (${greatInc})")
print(f"Greates Decrease in Profits: {greatDecMonth} (${greatDec})")

export_file_path = os.path.join("Analysis", "finAnalysis.txt")
with open(export_file_path, "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("----------------------------\n")
    analysis.write(f"Total Months: {num_months}\n")
    analysis.write(f"Total: ${totalPNL}\n")
    analysis.write(f"Average Change: ${round(avgChange, 2)}\n")
    analysis.write(f"Greates Increase in Profits: {greatIncMonth} (${greatInc})\n")
    analysis.write(f"Greates Decrease in Profits: {greatDecMonth} (${greatDec})\n")