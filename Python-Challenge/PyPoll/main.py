import os
import csv
import sys

election_csv = os.path.join(r"Resources\election_data.csv")

with open(election_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #stores header row
    header = next(csv_reader)

    total_votes = 0

    candidate_list = []

    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    
    for row in csv_reader:
        
        #total number of votes cast
        total_votes = total_votes + 1

        #list of candidates who received votes
        if row[2] not in candidate_list:

            candidate_list.append(row[2])

        #counts total votes for each candidate
        if row[2] == "Khan":

            khan_count = khan_count + 1

        elif row[2] == "Correy":

            correy_count = correy_count + 1

        elif row[2] == "Li":

            li_count = li_count + 1

        elif row[2] == "O'Tooley":

            otooley_count = otooley_count + 1

    #percentage of votes per candidate
    khan_calc = khan_count / total_votes
    correy_calc = correy_count / total_votes
    li_calc = li_count / total_votes
    otooley_calc = otooley_count / total_votes

    #percentage formatting
    khan_percentage = "{:.0%}".format(khan_calc)
    correy_percentage = "{:.0%}".format(correy_calc)
    li_percentage = "{:.0%}".format(li_calc)
    otooley_percentage = "{:.0%}".format(otooley_calc)

    #creates list of total votes per candidate
    candidate_votes = [khan_count, correy_count, li_count, otooley_count]

    max_vote = 0

    election_winner = ""

    for candidate, votes in zip(candidate_list, candidate_votes):
        #calculates winner of the election by popular vote
        if votes > max_vote:

            max_vote = votes

            election_winner = candidate

    #print analysis to terminal
    print("Election Results")
    print("----------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------")
    print(f'Khan: {khan_percentage} ({khan_count})')
    print(f'Correy: {correy_percentage} ({correy_count})')
    print(f'Li: {li_percentage} ({li_count})')
    print(f"O'Tooley: {otooley_percentage} ({otooley_count})")
    print("----------------------")
    print(f'Winner: {election_winner}')
    print("----------------------")
    
    #exports print statements as txt file to Analysis folder in PyPoll
    sys.stdout = open("PyPoll/Analysis/Analysis", "w")
    
    print("Election Results")
    print("----------------------")
    print(f'Total Votes: {total_votes}')
    print("----------------------")
    print(f'Khan: {khan_percentage} ({khan_count})')
    print(f'Correy: {correy_percentage} ({correy_count})')
    print(f'Li: {li_percentage} ({li_count})')
    print(f"O'Tooley: {otooley_percentage} ({otooley_count})")
    print("----------------------")
    print(f'Winner: {election_winner}')
    print("----------------------")