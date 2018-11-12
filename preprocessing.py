
#########################################################
#
# Programmer: Victoria Albanese
# Filename: preprocessing.py
# 
# Description: This file reads in the letters and words
# used for our bananagrams AI and does some preprocessing
# on both sets of items, namely:
#   - give each letter a frequency
#   - give each letter a prime 
#   - give each word a prime
#
#########################################################

import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd
import numpy as np
import time
from operator import itemgetter

#########################################################

# Reading & Formatting Data

words_df = pd.read_csv("Data/words.txt")
words_df['prime'] = pd.Series(np.zeros(len(words_df)), index=words_df.index)

letters_df = pd.read_csv("Data/letters.txt")
letters_df['frequency'] = pd.Series(np.zeros(len(letters_df)), index=letters_df.index)
letters_df['prime'] = pd.Series(np.zeros(len(letters_df)), index=letters_df.index)

words = words_df.values[:, 0:1]
letters = letters_df.values[:, 0:6]

#########################################################

# Prune Dictionary & Count Letters

start = time.time() 

rejects = []
for i, word in enumerate(words) :
    for letter in letters : 
        if (type(word[0]) is str) :   
            x = word[0].count(letter[0])
            letter[3]+= x
            if x > letter[1] :
                rejects.append(i)
valid_words = np.delete(words, rejects) 

end = time.time()
print "dictionary pruned & letters counted in ", (end - start), "seconds"

#########################################################

# Calculate Letter Frequencies

start = time.time() 

letters = np.flip(sorted(letters, key=itemgetter(3)), 0)
total_letters = np.sum(letters[:,3])  
for letter in letters :
    letter[3] = float(letter[3]) / float(total_letters)

end = time.time()
print "letter frequencies calculated in ", (end - start), "seconds"

#########################################################

# Calculate Letter Primes

start = time.time() 

count = 0
for num in range(2,103):
    if all(num%i!=0 for i in range(2,num)):
        letters[count][4] = num
        count+= 1

end = time.time()
print "letter primes calculated in ", (end - start), "seconds"

#########################################################

# Calculate Word Primes

start = time.time() 

letterDict = {}
for i in range(len(letters)) :
    letterDict[letters[i][0]] = letters[i][4] 
    
for word in words :
    product = 1
    if (type(word[0]) is str) :   
        for i, letter in enumerate(word[0]) : 
            product*= letterDict.get(letter)
        word[1] = product
 
end = time.time()
print "word primes calculated in ", (end - start), "seconds"
       
#########################################################

# Write Preprocessed Letters & Words to File

processed_letters_df = pd.DataFrame({
    'Letters':letters[:, 0], 
    'Occurances':letters[:, 1], 
    'Score':letters[:, 2], 
    'Frequency':letters[:, 3], 
    'Primes':letters[:, 4]})

processed_words_df = pd.DataFrame({
    'Words':words[:,0],
    'Primes':words[:,1]})

processed_letters_df.to_csv("Data/processed_letters.txt")
processed_words_df.to_csv("Data/processed_words.txt")

#########################################################

