# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:45:15 2016

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
    	word_dict = dict({word:string.count(word)})
    
    	
# Or add it to the dict with something like word_dict[word] = 1.
#       word_dict[word] = 1
    return word_dict

word_count("i am a stupid man and I am a dumb man and i am stuck")

#   !!!!! CORRECT !!!!!:
#	turn string with blank spaces into a dictionary 
#	of words(keys) and their wordcount(values)

def word_count(string):
    string = string.lower().split(" ")
    word_dict = {}
    for word in string:
    	word_dict[word] = string.count(word)
#       word_dict[word] = 1 
    return word_dict

word_count("i am a stupid man and I am a dumb man and i am stuck")

#	Seems to be right :D
