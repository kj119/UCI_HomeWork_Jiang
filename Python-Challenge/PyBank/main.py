import os
import csv

budget_csv = os.path.join(r"..\..\uci-irv-data-pt-08-2020-u-c\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    next(csv_reader)

    total_months = 0
    net_total = 0
    profit_losses = []

    for rows in csv_reader:
        
        #total number of months in dataset
        total_months = total_months + 1

        #net total of profit/losses
        net_total = net_total + int(rows[1])

        #creates list of profit/loss column
        profit_losses.append(int(rows[1]))

    #calculates profit/loss difference per month
    monthly_diff = [profit_losses[value + 1] - profit_losses[value] for value in range(len(profit_losses)-1)]

    

    
