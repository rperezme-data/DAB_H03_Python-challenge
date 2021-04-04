## Dependencies
import os
import csv

## Set dictionary for State Abbreviations
## Reference: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

## Set initial values
employee_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

## IMPORT FROM CSV FILE
## Define path for CSV file
input_path = os.path.join('Resources','employee_data.csv')

## Read CSV file
with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
        
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    ## Skip CSV header 
    next(csv_reader)
        
    ## Loop through CSV rows & Change format
    for row in csv_reader:
            
            ## Store 'Emp ID' column as is
            employee_id.append(row[0])

            ## Split 'Name' column into separate 'First Name' and 'Last Name' columns
            name_split = row[1].split(sep=' ')
            first_name.append(name_split[0])
            last_name.append(name_split[1])

            ## Re-write 'DOB' data into 'MM/DD/YYYY' format
            dob_split = row[2].split(sep='-')
            dob.append(dob_split[1] + "/" + dob_split[2] + "/" + dob_split[0])

            ## Re-write 'SSN' data hiding first 5 numbers from view
            ssn_split = row[3].split(sep='-')
            ssn.append("***-**-" + ssn_split[2])

            ## Re-write 'State' data into two-letter abbreviations
            state.append(us_state_abbrev[row[4]])

# Set new header (according to new format)
header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]

# Zip all lists together into tuples
format_conversion = zip(employee_id, first_name, last_name, dob, ssn, state)


## EXPORT TO CSV FILE
## Define path for CSV file
output_path = os.path.join('Analysis','PyBoss_Conversion.csv')

## Write CSV file
with open(output_path, mode='w', newline='', encoding='utf-8') as csv_file:

    # Initialize csv.writer
    csv_writer = csv.writer(csv_file, delimiter=',')

    # Write first row (column headers)
    csv_writer.writerow(header)

    # Write zipped rows (format conversion)
    csv_writer.writerows(format_conversion)



