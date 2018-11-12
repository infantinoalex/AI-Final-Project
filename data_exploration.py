
# coding: utf-8

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

start = time.time() 
end = time.time()
print "calculations done in ", (end - start), "seconds"

#########################################################

# Prune Dictionary & Count Letters

rejects = []
for i, word in enumerate(words) :
    for letter in letters : 
        if (type(word[0]) is str) :   
            x = word[0].count(letter[0])
            letter[3]+= x
            if x > letter[1] :
                rejects.append(i)
valid_words = np.delete(words, rejects) 

#########################################################

# Calculate Letter Frequencies

letters = np.flip(sorted(letters, key=itemgetter(3)), 0)
total_letters = np.sum(letters[:,3])  
for letter in letters :
    letter[3] = float(letter[3]) / float(total_letters)

#########################################################

# Calculate Letter Primes

count = 0
for num in range(2,103):
    if all(num%i!=0 for i in range(2,num)):
        letters[count][4] = num
        count+= 1

#########################################################

# Calculate Word Primes

letterDict = {}
for i in range(len(letters)) :
    letterDict[letters[i][0]] = letters[i][4] 
    
for word in words :
    product = 1
    if (type(word[0]) is str) :   
        for i, letter in enumerate(word[0]) : 
            product*= letterDict.get(letter)
        word[1] = product
        
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

    
wordDict = {}      
for word in words :
    wordDict[word[1]] = word[0]

product = 1
anchor = 'A'
word = 'EVBEMTSBDGSMIRT'
anchorDict = {}
possible_words = list()

start = time.time()

# get the prime number associated with the hand + the anchor
for i, letter in enumerate(word + anchor) : 
    product*= letterDict.get(letter)
print product, " : ", word

# SEARCH PHASE 1
# get all possible words involving the anchor
for key in wordDict :
    if (key % letterDict.get(anchor) == 0) :
        anchorDict[key] = wordDict.get(key)        
        
# SEARCH PHASE 2        
# get all words from those using only letters from the hand        
for key in anchorDict :
    if (product % key == 0) :
        possible_words.append(anchorDict.get(key))        
    
end = time.time()

print len(anchorDict)
print len(possible_words)
print possible_words
print "---"
print "calculations done in ", (end - start), "seconds"

