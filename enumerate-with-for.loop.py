##################################################
###############   Coding Exercise  ###############
##################################################

# Use built-in enumerate() function to make use of
# e.g print a corresponding index with a list-item
##################################################

# Add +1 to index to start counting at 1 (not 0)

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item


##################################################
# END