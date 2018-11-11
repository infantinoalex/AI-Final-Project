
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from operator import itemgetter


# In[2]:


# Read in the dictionary as a pd dataframe
filepath = "C:\Users\Victoria\Documents\Victoria's Reports\Graduate\Semester01_Fall2018\Artificial_Intelligence\Project"
words_df = pd.read_fwf(filepath + "\dictionary.txt")
letters_df = pd.read_csv(filepath + "\letters.csv")
letters_df['frequency'] = pd.Series(np.zeros(len(letters_df)), index=letters_df.index)

# Format the data as list
words = words_df.values[:, 0].tolist()
letters = letters_df.values[:, [0, 1, -1]].tolist()

#words
#letters


# In[3]:


# generate the reject words which cannot be included 
# due to an impossible amount of letters; also count 
# the number of letters in all of the words
rejects = []
        
for word in words :
    for letter in letters : 
        if (type(word) is str) :
            x = word.count(letter[0])
            letter[2]+= x
            if x > letter[1] :
                rejects.append(word)
        
# remove the rejects from the word list
for reject in rejects :
    words.remove(reject)
        
print len(rejects), " rejects found"
print len(words), " dictionary size"
print rejects


# In[4]:


letters.sort(reverse=True, key=itemgetter(2))

total_letters = 0
for letter in letters :
    total_letters+= letter[2]
    
for letter in letters :
    letter[2] = float(letter[2]) / float(total_letters)
    print letter[0], " has frequency ", letter[2]


# In[5]:


objects = [letter[0] for letter in letters]
y_pos = np.arange(len(objects))
performance = [letter[2] for letter in letters]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.title('Letter Frequency')
 
plt.show()


# In[6]:


primes = []
for num in range(2,103):
    if all(num%i!=0 for i in range(2,num)):
       primes.append(num)

letterPrimeDict = {}
    
for i in range(len(letters)) :
    letterPrimeDict[letters[i][0]] = primes[i]
    print letters[i][0], " : ", primes[i]


# In[7]:


dictionary = {}
        
for word in words :
    product = 1
    for i, letter in enumerate(word) : 
        product*= letterPrimeDict.get(letter)
    dictionary[product] = word
        
for key in dictionary :
    print key, " : ", dictionary.get(key)


# In[ ]:


product = 1
word = 'EVBEMTSBDGSMIRT'

product = 1
for i, letter in enumerate(word) : 
    product*= letterPrimeDict.get(letter)
print product, " : ", word

possible_words = list()
for key in dictionary :
    if ((float(product) / float(key)).is_integer()) :
        possible_words.append(dictionary.get(key))
        
print possible_words
print len(possible_words)

