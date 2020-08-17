import os
import csv


file_path = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

tot_votes = 0
with open(file_path, "r") as data:
    reader = csv.reader(data, delimiter = ",")
    header = next(reader)
    for row in reader:
        tot_votes += 1


print(tot_votes)
