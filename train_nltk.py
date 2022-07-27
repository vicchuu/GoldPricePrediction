

import json
from nltk_utils import tokenise,stemming

with open("intents.json",'r') as f:
    intents = json.load(f) #dict type object




all_words =[]

tags =[]

xy=[]

"""Tokenization ..."""
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    #all_words.append(intent)
    for a in intent['patterns']:
        words = tokenise(a)
        all_words.extend(words)
        xy.append((words,tag))

"""Stemming and lowering"""
"""And also excluding punctuation mark"""


ignore_words = ["?",":",";","(",")","*","%","#","@","!","$","{","}","[","]","_","-","'",'"']

print(len(all_words))
all_words = [stemming(w) for w in all_words if w not in ignore_words]

print(len(all_words))


"""its time for bag of words"""

xtrain =[]
ytrain = []