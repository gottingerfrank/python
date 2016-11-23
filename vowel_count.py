#	edX MIT 6.00.1x - Problem Set 1
#	Count the number of vowels 'aeiou' contained
#	in a given string s of lowercase characters
#	valid vowels are: 'a,e,i,o,u' 

# 	It is assumed string s is already given! 



def count_vowels(s):
	"""Count the number of vowels 'aeiou' contained
   in a given string s of lowercase characters
   valid vowels are: 'a,e,i,o,u'"""
	v_a=s.count('a')
	v_e=s.count('e')
	v_i=s.count('i')
	v_o=s.count('o')
	v_u=s.count('u')
	num_vowels=v_a+v_e+v_i+v_o+v_u
	print("Number of vowels:",num_vowels)
	return num_vowels	

s='muffduffingobblah'


count_vowels(s)

















