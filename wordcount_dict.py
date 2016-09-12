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

###################

#	ALT-try

#	def word_count(string):
#		string = string.lower().split(" ")
#		word_dict = dict(string)
#		for word in string:

#	STUCK !!!

###################

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.


def word_count(string):
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
    string = string.lower().split(" ")

#   word_count = 0
    
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
    for word in string:
    	word_dict = dict((word),1)
    	
# Or add it to the dict with something like word_dict[word] = 1.
#       word_dict[word] = 1
    return word_dict

word_count("i am a stupid man and I am a dumb man and i am stuck")



#		word_dict = {{}:{}}.format(word,1)








