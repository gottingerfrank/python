##################################################
###############   Coding Exercise  ###############
##################################################

# Codecademy: Python Course(Python2) - Dicts/Lists

##################################################

inventory = {
    'pocket':['seashell', 'strange berry', 'lint'],
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], 
# Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }

backpack_value = inventory['backpack']
backpack_value.sort()

# or this works, too...
inventory['backpack'].sort()

# remove a list value in one of the dict-values
inventory['backpack'].remove('dagger')

##################################################
# END

1