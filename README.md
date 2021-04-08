# Python-challenge
This set of four Python scripts are basic examples of the Data Analysis workflow:
1) Read data from input files (csv/txt)
2) Analyse data (looping through rows, computing and summarizing)
3) Write results into output files (csv/txt)
4) Print results to terminal

## 1. PyBank
This script reads financial records from a CSV file with the following structure:
| Date | Profit/Losses
| --- | --- 

Using a `for` loop, the script counts the number of months, computes the sum of Profit/Losses while, and computes the Profit/Losses change for each month (in relation to the last month) and stores it in a dictionary: *{month (key) : P/L change (value)}*.

To summarize the Profit/Losses change information, the script computes the *P/L average change* and gets the *Greatest increase in Profits* and the *Greatest increase in Profits* (or Greatest increase in Losses) over the entire period.

At the end, the script generates a report through a function and writes the report to an output file (txt) and print it to the terminal.

## 2. PyPoll
This script reads election data form a CSV file with the following structure:
| Voter ID | County | Candidate
| --- | --- | ---

Using a `for` loop, the script stores (and summarizes) the election data in a dictionary: *{candidate (key) : number of votes (value)}*. If a new candidate is detected, it adds the name as a key and counts the vote. If no new candidate is detected, it accumulates the vote for the existing one. After the loop is complete, the script computes the total number of votes of all candidates.

The dictionary structure allows to generate the election results using *{key:value}* pairs to display the complete list of candidates who received votes, the percentage of votes and the total number of votes each candidate won. The winner candidate is selected calling the `max()` and `get()` built-in functions.

At the end, the script generates a report through a function and writes the report to an output file (txt) and print it to the terminal.

## 3. PyBoss







