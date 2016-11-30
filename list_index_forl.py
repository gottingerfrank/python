##################################################
###############   Coding Exercise  ###############
##################################################

# Python 2 - Experiment w. Lists/Indices
##################################################


# make list and print original list
listy_boy = list(range(10))
print listy_boy

# function to  multiply every list item
def doubleitem_list(l):
	"""takes in a list of only numbers and 
	multiplies every list item.Returns
	modified list"""
	for i in range(len(listy_boy)):
		listy_boy[i] *= 2
	return listy_boy

# original list before function
print listy_boy 

doubleitem_list(listy_boy)

# list after function

print listy_boy

##################################################

listy_girl = list("1923425304583743582345556")

# print original list with ints as strings still
print listy_girl

for i in range(len(listy_girl)):
	listy_girl[i] = int(listy_girl[i])

# print list (yeah basically pointless, just trying stuff out...)
print listy_girl



# (...)

##################################################
# END