import os
import csv


file_path = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

tot_votes = 0
results = {}
with open(file_path, "r") as data:
    reader = csv.reader(data, delimiter = ",")
    header = next(reader)
    for row in reader:
        tot_votes += 1
        candidate = row[2]
        if candidate in results.keys():
            results[candidate] += 1
        else:
            results[candidate] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_votes}")
print("-------------------------")
maxPct = 0
for cand, votes in results.items():
    pct = round(((votes/tot_votes)*100),3)
    if pct > maxPct:
        maxPct = pct
        winner = cand
    print(f"{cand}: {pct}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


export_file_path = os.path.join("Analysis", "pollAnalysis.txt")
with open(export_file_path, "w") as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Total Votes: {tot_votes}\n")
    analysis.write("-------------------------\n")
    maxPct = 0
    for cand, votes in results.items():
        pct = round(((votes/tot_votes)*100),3)
        if pct > maxPct:
            maxPct = pct
            winner = cand
        analysis.write(f"{cand}: {pct}% ({votes})\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Winner: {winner}\n")
    analysis.write("-------------------------\n")