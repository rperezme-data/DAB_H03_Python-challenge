## Dependencies
import os
import re

## Set initial values


## IMPORT DATA FROM TXT FILE
## Define path for TXT file
input_path = os.path.join('Resources','paragraph_data.txt')

## Read TXT file
with open(input_path, mode='r', newline='', encoding='utf-8') as txt_file:

    ## Store text (paragraph) from TXT file
    paragraph = txt_file.read()


## Count number of words
word_list = re.findall('\w+', paragraph)

## Count number of sentences
# sentence_list = re.split('\.', paragraph)
sentence_list = re.split('(?<=[.!?]) +', paragraph)

# print(word_list)
print(len(word_list))

# print(sentence_list)
print(len(sentence_list))
