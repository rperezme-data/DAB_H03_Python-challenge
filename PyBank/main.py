## Dependencies
import os
import csv

# Set boolean for first month
first_month = True

## Set initial values
month_count = 0
total_pnl = 0
last_pnl = 0

## Set dictionary {month (key) : P/L change (value)}
pnl_change = {}


## IMPORT DATA FROM CSV FILE
## Define path for CSV file
input_path = os.path.join('Resources','budget_data.csv')

## Read CSV file
with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    ## Skip CSV header 
    next(csv_reader)
    
    ## Loop through CSV rows
    for row in csv_reader:

            ## Count number of months (rows)
            month_count += 1
            
            ## Sum Profits/Losses
            total_pnl += float(row[1])

            ## Skip first month since there is no P/L change for the initial value
            if first_month == False:

                ## Compute Profits/Losses change for current month [Change = Current - Last] and Store month as key
                pnl_change[(row[0])] = float(row[1]) - last_pnl

            ## Store current P/L for next month's analysis
            last_pnl = float(row[1])

            ## Set variable for subsequent months 
            first_month = False


## P/L CHANGE SUMMARY

## Compute P/L average change [AVG = sum(n) / n] 
avg_change = sum(pnl_change.values()) / (len(pnl_change))

## Get P/L change max increase & Store as tuple (month, value)
max_increase = (max(pnl_change, key=pnl_change.get), max(pnl_change.values()))

## Get P/L change max decrease & Store as tuple (month, value)
max_decrease = (min(pnl_change, key=pnl_change.get), min(pnl_change.values()))


## GENERATE REPORT
## Generate Report as a function
def gen_report():

    ## Financial Analysis Report
    report = [
        "Financial Analysis",
        "------------------------------",
        f"Total months: {month_count}",
        f"Total: ${total_pnl:,.0f}",
        f"Average Change: ${avg_change:,.2f}",
        f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]:,.0f})",
        f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]:,.0f})"
        ]
    
    ## Return Report as a list
    return (report)


## EXPORT REPORT TO TXT FILE
## Define path for TXT file
output_path = os.path.join('Analysis','PyBank_Report.txt')

## Write TXT file
with open(output_path, mode='w', newline='', encoding='utf-8') as txt_file:
    ## Write line-by-line loop
    for line in gen_report():
        txt_file.write(line + "\n")


## PRINT REPORT TO TERMINAL
## Print line-by-line loop
for line in gen_report():
    print(line)
