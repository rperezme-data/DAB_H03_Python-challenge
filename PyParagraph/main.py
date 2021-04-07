## Dependencies
import os
import re

## Set initial values
letter_count = 0
words_per_sentence = []

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


print(sentence_count)
print(word_count)
print(letter_count)


# print(word_list)
# print(len(word_list))

# print(sentence_list)
# print(len(sentence_list))

# for item in sentence_list:
#     words_per_sentence.append(len(re.findall('\w+', item)))



# print(sum(words_per_sentence))


# for item in word_list:
#     letter_count += (len(item))

# # print(letter_count / len(word_list))

# print (len(re.findall('\w', paragraph)))