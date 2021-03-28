## Dependencies
import os
import csv

## Set initial values
vote_count = 0

## READ DATA FROM CSV FILE
## Define path for CSV file
input_path = os.path.join('Resources','election_data.csv')

## Read CSV file
with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    ## Get CSV header 
    csv_header = next(csv_reader)
    ## Loop through CSV rows

    for row in csv_reader:

        ## Count number of votes (rows)
        vote_count += 1
   

print(vote_count)

