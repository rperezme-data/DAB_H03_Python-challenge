## Dependencies

import os
import csv

## Define path for csv file
csv_path = os.path.join('Resources','budget_data.csv')
#print(csv_path)

## Set initial values
month_count = 0

##
with open(csv_path, newline='', encoding='utf-8') as csv_file:
    #print(csv_file)
    
    ##
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    ## Get CSV header 
    csv_header = next(csv_reader)
    print(csv_header)

    ## Loop through CSV rows
    for row in csv_reader:
            #print(row)

            ## Count number of months (rows)
            month_count += 1
    
    print (month_count)