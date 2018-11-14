import os
import sys 
unitTestPath = os.path.dirname(__file__) + "/../Source"
sys.path.append(unitTestPath)

#########################################################
#
# Programmer: Victoria Albanese
# Filename: search.py
# 
# Description: This file reads in the processed letters 
# and words files and searches for valid words to play
#
#########################################################

import os
import time
from operator import itemgetter

import numpy as np
import pandas as pd

#########################################################

# Reading & Formatting Data

directory = os.path.dirname(__file__)

words_df = pd.read_csv(directory + "/../Data/processed_words.txt")
words = words_df.values[:, 0:2]
wordDict = {}      
for word in words :
    wordDict[word[1]] = word[0]

letters_df = pd.read_csv(directory + "/../Data/processed_letters.txt")
letters = letters_df.values[:, 0:6]
letterDict = {}      
for letter in letters :
    letterDict[letter[0]] = letter[4]

#########################################################

# Setup & Search a Sample Hand    

product = 1
anchor = 'Q'
word = 'EVBEMTSBDGSMIRT'
anchorDict = {}
possible_words = []

for i, letter in enumerate(word + anchor) : 
    x = letterDict.get(letter)
    product*= x
print(product, " : ", word)

start = time.time()

# SEARCH PHASE 1
# get all possible words involving the anchor
a = letterDict.get(anchor)
for key in wordDict :
    if (int(key) % int(a) == 0) :
        anchorDict[key] = wordDict.get(key)        
        
# SEARCH PHASE 2        
# get all words from those using only letters from the hand        
for key in anchorDict :
    if (int(product) % int(key) == 0) :
        possible_words.append(anchorDict.get(key))        
    
end = time.time()

print("anchor dictionary length:", len(anchorDict))
print("number of possible words:", len(possible_words))
print(possible_words)
print("---")
print("calculations done in", (end - start), "seconds")

#########################################################
