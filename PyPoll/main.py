## Dependencies
import os
import csv


## Set initial values
vote_count = 0
results = {}


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
   
        ## Check for new candidate
        if row[2] not in results:
            ## Add new candidate (key) and count first vote
            results[row[2]] = 1
        else:
            ## Accumulate vote for existing candidate
            results[row[2]] += 1


## PRINT RESULTS
## Print Results as a function
def print_results():

    results_header = [
        "Election Results",
        "------------------------------",
        f"Total Votes: {vote_count:,}",
        "------------------------------"
        ]

    results_candidates = []
    for key, value in results.items():
        results_candidates.append(f"{key}: {value/vote_count:.3%} ({value:,})")
    
    results_winner = [
        "------------------------------",
        f"Winner: {max(results, key=results.get)}",
        "------------------------------"
        ]   

    return (results_header + results_candidates + results_winner)


## PRINT RESULTS TO THE TERMINAL

for line in print_results():
    print(line)

# print(print_results())