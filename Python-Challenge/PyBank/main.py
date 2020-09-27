import os
import csv

budget_csv = os.path.join(r"..\..\uci-irv-data-pt-08-2020-u-c\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    next(csv_reader)

    total_months = 0
    net_total = 0
    profit_losses = []
    dates = []

    for rows in csv_reader:
        
        #total number of months in dataset
        total_months = total_months + 1

        #net total of profit/losses
        net_total = net_total + int(rows[1])

        #creates list of profit/loss column
        profit_losses.append(int(rows[1]))

        if total_months > 1:
            dates.append(rows[0])

    #calculates profit/loss difference per month
    monthly_diff = [profit_losses[value + 1] - profit_losses[value] for value in range(len(profit_losses)-1)]

    #solution for average of changes in profit/loss over entire period
    avg_chg_profitLoss = sum(monthly_diff) / (len(profit_losses)-1)
    
    max_monthly_diff = 0
    min_monthly_diff = 0

    max_date = ""
    min_date = ""
    
    for date, values in zip(dates, monthly_diff):

        #calculates greatest increase in profits over entire period
        if values > max_monthly_diff:

            max_monthly_diff = values

            max_date = date

        #calculates decrease in losses over entire period
        elif values < min_monthly_diff:

            min_monthly_diff = values

            min_date = date

    print("Financial Analysis"
    
    

    

    
