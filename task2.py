from itertools import count
import os
import shutil
import multiprocessing
directory = "tmp-zad2"

try:
    os.mkdir(directory)
except FileExistsError:
    print('Katalog tmp-zad2 istnieje, czyszczę zawartość')
    shutil.rmtree(directory)
    os.mkdir(directory)

# file = open('./wc_1000_100_10.dat', 'r')
file = open('./example.dat', 'r')
dic = {}
lettersFilesDict = {}
letters = []


# Creating file for every letter
while True: # loop for words
    # loop for characters
    word = ''
    while True:
        char = file.read(1)

        if char == ',' or char == '\n' or char == '':
            break
        word += char
        
    if word == 'ENDOFDATA':
        break
    if word[0] not in dic:
        dic[word[0]] = open(directory + '/' + word[0], 'a+')
        dic[word[0]].write(word + '\n')
    else:
        dic[word[0]].write(word  + '\n')

file.close()

# Sorting Files

for letter, f in dic.items():
    f.flush() # saving words
    f.seek(0) # set the position to the beggining of the file
    # items = f.readlines()
    dict_for_letter = {}
    while True:
        word = f.readline()
        if not word:
            break
        if word in dict_for_letter:
            dict_for_letter[word] += 1
        else:
            dict_for_letter[word] = 1
        

    print(dict_for_letter)
    f.close()
# function to count the occurence of words in dictionary
# it print 20 most common words and 20 least common words
# def print_dic(dic):
#     print('20 most common words:')
#     for i in range(20):
#         max_key = max(dic, key=dic.get)
#         print(max_key, dic[max_key])
#         del dic[max_key]
#     print('20 least common words:')
#     for i in range(20):
#         min_key = min(dic, key=dic.get)
#         print(min_key, dic[min_key])
#         del dic[min_key]
#     print('\n')
# print_dic(dic)