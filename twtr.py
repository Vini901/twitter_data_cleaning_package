import pandas as pd 
import numpy as np 
import re
import string
import nltk
from nltk.stem.porter import *
nltk.download('stopwords')
from nltk.corpus import stopwords

def remove_pattern(inp_txt,pattern):
    r=re.findall(pattern,inp_txt)
    for i in r:
        inp_txt=re.sub(i,"",inp_txt)
    return inp_txt

def rmve_stopwords_punctation(msg):
    nopunc =[char for char in msg if char not in string.punctuation]
    nopunc=''.join(nopunc)
    return ' '.join([word for word in nopunc.split() if word.lower() not in stopwords.words('english')])


def remove_small_words(msg,le):
    msg=" ".join([m for m in msg.split(' ') if len(m)>le])
    return msg

def tokenisation(msg):
    return msg.split()

def stemming_process(raw_data):
    stemmer = PorterStemmer()
    tokenized =[stemmer.stem(i) for i in raw_data] # stemming
    return " ".join(tokenized)

