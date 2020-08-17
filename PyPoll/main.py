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
for cand, votes in results.items():
    print(f"{cand}: {round(((votes/tot_votes)*100),3)}% ({votes})")
print("-------------------------")
