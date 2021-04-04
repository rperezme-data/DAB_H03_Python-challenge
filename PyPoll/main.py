## Dependencies
import os
import csv

## Set dictionary {candidate (key) : number of votes (value)}
results_dict = {}


## IMPORT DATA FROM CSV FILE
## Define path for CSV file
input_path = os.path.join('Resources','election_data.csv')

## Read CSV file
with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    ## Skip CSV header 
    next(csv_reader)
    
    ## Loop through CSV rows
    for row in csv_reader:
        
        ## Check for new candidate
        if row[2] not in results_dict:
            ## Add new candidate (key) and count first vote (value)
            results_dict[row[2]] = 1
        else:
            ## Accumulate vote (value) for existing candidate
            results_dict[row[2]] += 1

## Compute total votes = Sum of votes (values) of all candidates
vote_count = sum(results_dict.values())

## GENERATE RESULTS
## Generate Results as a function
def gen_results():

    ## Results report header & Total Votes
    results_header = [
        "Election Results",
        "------------------------------",
        f"Total Votes: {vote_count:,}",
        "------------------------------"
        ]

    ## Results report votes per candidate
    results_candidates = []
    for key, value in results_dict.items():
        results_candidates.append(f"{key}: {value/vote_count:.3%} ({value:,})")

    ## Results report winner (candidate with most votes)
    results_winner = [
        "------------------------------",
        f"Winner: {max(results_dict, key=results_dict.get)}",
        "------------------------------"
        ]

    ## Return Results as a collection of lists
    return (results_header + results_candidates + results_winner)


## EXPORT RESULTS TO TXT FILE
## Define path for TXT file
output_path = os.path.join('Analysis','PyPoll_Results.txt')

## Write TXT file
with open(output_path, mode='w', newline='', encoding='utf-8') as txt_file:
    ## Write line-by-line loop
    for line in gen_results():
        txt_file.write(line + "\n")


## PRINT RESULTS TO TERMINAL
## Print line-by-line loop
for line in gen_results():
    print(line)
