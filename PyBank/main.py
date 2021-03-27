## Dependencies

import os
import csv

## Define path for csv file
csv_path = os.path.join('Resources','budget_data.csv')
print(csv_path)


with open(csv_path, newline='') as csv_file:
    print(csv_file)
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
            print(row)
