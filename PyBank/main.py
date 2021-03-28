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
pnl_change = 0
pnl_change_list = []

max_increase_value = 0
max_increase_month = ""
max_decrease_value = 0
max_decrease_month = ""

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
                pnl_change = float(row[1]) - last_pnl
                pnl_change_list.append(pnl_change)

                ##
                if pnl_change > max_increase_value:
                    max_increase_value = pnl_change
                    max_increase_month = row[0]

                if pnl_change < max_decrease_value:
                    max_decrease_value = pnl_change
                    max_decrease_month = row[0]

            ## Store current P/L for next month's analysis
            last_pnl = float(row[1])

            ## Set variable for subsequent months 
            first_month = False


## Compute P/L average change [AVG = sum(n) / n] 
avg_change = sum(pnl_change_list) / len(pnl_change_list)


def print_report():
    ## Print Report
    print()
    print("Financial Analysis")
    print("------------------------------")
    print (f"Total months: {month_count}")
    print (f"Total: ${total_pnl:,.0f}")
    print ("Average Change: ${:,.2f}".format(avg_change))
    print (f"Greatest Increase in Profits: {max_increase_month} (${max_increase_value:,.0f})")
    print (f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease_value:,.0f})")
    print()

print_report()

# str_value = 15.34
# int_value = int(str_value)
# print (int_value)