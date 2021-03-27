## Dependencies

import os
import csv

## Define path for csv file
csv_path = os.path.join('Resources','budget_data.csv')
# print(csv_path)

## Set initial values
month_count = 0
total_pnl = 0

## Read CSV file
with open(csv_path, newline='', encoding='utf-8') as csv_file:
    # print(csv_file)
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)

    ## Get CSV header 
    csv_header = next(csv_reader)
    # print(csv_header)

    ## Loop through CSV rows
    for row in csv_reader:
            #print(row)

            ## Count number of months (rows)
            month_count += 1

            ## Sum Profits/Losses
            total_pnl += int(row[1])
    

    ## Print Analysis Results
    print()
    print("Financial Analysis")
    print("------------------------------")
    print (f"Total months: {month_count}")
    print (f"Total: ${total_pnl:,}")