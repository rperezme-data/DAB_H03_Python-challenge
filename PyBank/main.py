## Dependencies
import os
import csv

## Define path for csv file
csv_path = os.path.join('Resources','budget_data.csv')
# print(csv_path)

# Set variable for first month
first_month = True

## Set initial values
month_count = 0
total_pnl = 0
last_pnl = 0
pnl_change = []


## Read CSV file
with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
    # print(csv_file)
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)

    ## Get CSV header 
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
    
    ## Loop through CSV rows
    for row in csv_reader:
            #print(row)

            ## Count number of months (rows)
            month_count += 1

            ## Sum Profits/Losses
            total_pnl += float(row[1])

            ## Skip first month since there is no P/L change for the initial value
            if first_month == False:

                ## Compute Profits/Losses change for current month [Change = Current - Last]
                pnl_change.append(float(row[1]) - last_pnl)
                

            ## Store current P/L for next month's analysis
            last_pnl = float(row[1])

            ## Set variable for subsequent months 
            first_month = False



## Compute P/L average change [AVG = sum(n) / n] 
avg_change = sum(pnl_change) / len(pnl_change)


## Print Analysis Results
print()
print("Financial Analysis")
print("------------------------------")
print (f"Total months: {month_count}")
print (f"Total: ${total_pnl:,.0f}")
print ("Average Change: ${:,.2f}".format(avg_change))
print()

# str_value = 15.34
# int_value = int(str_value)
# print (int_value)