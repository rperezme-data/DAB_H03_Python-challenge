## Dependencies
import os
import re


## IMPORT DATA FROM TXT FILE
## Define path for TXT file
input_path = os.path.join('Resources','paragraph_data.txt')

## Read TXT file
with open(input_path, mode='r', newline='', encoding='utf-8') as txt_file:

    ## Store text (paragraph) from TXT file
    paragraph = txt_file.read()

## PARAGRAPH ANALYSIS
## Count number of letters
letter_count = len(re.findall('\w', paragraph))

## Count number of words
word_count = len(re.findall('\w+', paragraph))

## Count number of sentences
sentence_count = len(re.split('(?<=[.!?]) +', paragraph))


## GENERATE REPORT
## Generate Report as a function
def gen_report():

    ## Paragraph Analysis Report
    report = [
        "Paragraph Analysis",
        "------------------------------",
        f"Approximate Word Count: {word_count}",
        f"Approximate Sentence Count: {sentence_count}",
        f"Average Letter Count: {letter_count / word_count:.1f}",
        f"Average Sentence Length: {word_count / sentence_count:.1f}"
        ]
    
    ## Return Report as a list
    return (report)
