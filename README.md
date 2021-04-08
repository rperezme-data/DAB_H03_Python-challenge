# Python-challenge
This set of four Python scripts are basic examples of the Data Analysis workflow:
1) Read data from input files (csv/txt)
2) Analyse data (looping through rows, computing and summarizing)
3) Write results into output files (csv/txt)
4) Print results to terminal

## 1. PyBank
This script reads financial records from a CSV file, with the following Headers:
| Date | Profit/Losses
| --- | --- 

Using a `for` loop, the script counts the number of months, computes the sum of Profit/Losses while, and computes the Profit/Losses change for each month (in relation to the last month) and stores it in a dictionary `{month (key) : P/L change (value)}`.

To summarize the Profit/Losses change information, the script computes the *P/L average change* and gets the *Greatest increase in Profits* and the *Greatest increase in Profits* (or Greatest increase in Losses) over the entire period.

At the end, the script generates a report through a function and writes the report to an output file (txt) and print it to the terminal.







