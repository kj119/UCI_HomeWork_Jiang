import os
import csv

election_csv = os.path.join(r"..\..\uci-irv-data-pt-08-2020-u-c\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv")

with open(election_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    next(csv_reader)

    total_votes = 0

    candidate_list = []
    
    for row in csv_reader:
        
        #total number of votes cast
        total_votes = total_votes + 1

        #list of candidates who received votes
        if row[2] not in candidate_list:

            candidate_list.append(row[2])

    