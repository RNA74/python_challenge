import os
import csv

total_month = 0
total_profit = 0
monthly_change = []

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
csv_path = os.path.join("..",'PyBank','Resources','budget_data.csv')

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    header = next(csvreader)
    prv_change = 0


    for row in csvreader:
        total_month += 1
        total_profit += int(row[1])
        net_change = int(row[1])-prv_change
        prv_change = int(row[1])
        monthly_change.append(net_change)

    average_change = sum(monthly_change)/len(monthly_change)
    greatest_increase = max(monthly_change)
    greatest_decrease = min (monthly_change)

    print(f"Total month: {total_month}")
    print(f"Total Profit: {total_profit}")
    print(f"Average change: {average_change}")
    print(f"Greatest increase in profit: {greatest_increase}")
    print(f"Greater decrease in profit: {greatest_decrease}")