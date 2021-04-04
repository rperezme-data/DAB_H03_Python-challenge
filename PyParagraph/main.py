## Dependencies
import os
import re

## Set initial values


## IMPORT DATA FROM TXT FILE
## Define path for TXT file
input_path = os.path.join('Resources','paragraph_data.txt')

## Read TXT file
with open(input_path, mode='r', newline='', encoding='utf-8') as txt_file:
        
        paragraph = txt_file.read()


print(paragraph)