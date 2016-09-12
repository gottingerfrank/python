# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:34:38 2016

@author: mellowcat
"""

def word_count(string):
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
    string = string.lower().split(" ")

#   word_count = 0
    
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
    for word in string:
    	word_dict = {{}:{}}.format(word,string.count(word))
# Or add it to the dict with something like word_dict[word] = 1.
#       word_dict[word] = 1
    return word_dict

word_count("i am a stupid man and I am a dumb man and i am stuck")


