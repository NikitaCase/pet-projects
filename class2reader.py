import csv
import random


with open("tube\\budget.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
        break

    #for row in file:
     #   print(row)
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
