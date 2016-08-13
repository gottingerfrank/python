#   ** Pig Latin Translator **
#   ** coding exercise **
#   ** codecademy free courses | <3 ** 

#   Word in PigLatin = 1st letter put to
#   End of word + 'ay'added ...


#	Function to check if characters contained in string

def isalpha(x):
	"""Function to sort out if word 'original' entered
	by user is made up of only characters"""

	for i in original:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			return True
		else:
			return False


def pigLatTranslate(original):
	"""PigLatin translator"""
	
	if len(original) > 0 and original.isalpha():
		word = original.lower()
		first = word[0]
		new_word = word + first + pyg
		new_word = new_word[1:len(new_word)]
		print new_word
		return new_word
	else:
	    print 'empty'

pyg = 'ay'

original = raw_input('Enter a word:').lower()

pigLatTranslate(original)


