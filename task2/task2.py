from itertools import count
from collections import Counter
import os
import shutil
import time

directory = "tmp-task2"

try:
    os.mkdir(directory)
except FileExistsError:
    print('Directory tmp-task2 exists, removing content')
    shutil.rmtree(directory)
    os.mkdir(directory)



start_time = time.time()
file = open('./wc_1000_100_10.dat', 'r')
#file = open('./example.dat', 'r')
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
print('ALL WORDS WRITTEN')
# Sorting Files

counters = {}

for letter, f in dic.items():
    f.flush() # saving words
    f.seek(0) # set the position to the beggining of the file
    dict_for_letter = {}
    cnt = Counter()
    while True:
        word = f.readline()
        if not word:
            break
        cnt[word] += 1
    most_common = cnt.most_common()
    counters.update(most_common[:20])
    counters.update(most_common[-20:])
    print('FINISHED COUNTING WORDS FOR LETTER:', letter)
    f.close()

final_most_common = Counter(counters).most_common()
most_common_20 = final_most_common[:20]
least_common_20 = final_most_common[-20:]
print('MOST COMMON', most_common_20)
print('LEAST COMMON', least_common_20)
print('IT TOOK', time.time() - start_time, 'SECONDS')