student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data)
data_dict = {row.letter:row.code for index,row in data.iterrows()}
print(data_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

not_finish = True
while not_finish:
    word_user = input('Enter a word: ').upper()
    try:
        output_list = [data_dict[letter] for letter in word_user]
        print(output_list)
        not_finish = False
    except: 
        print('Sorry, only letters in the alphabet please')
