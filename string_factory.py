#	treehouse - Collections
#	Create a function that takes 2 arguments:
#	a list of dictionaries and a string

#	GIVEN:

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

#   create function with 2 arguments

def string_factory(dicts, string):

#   Return new list build by using .format() on the string,
#   filled in by each of the dictionaries in the list

	new_list = []
	for a_dict in dicts:
		a_string = string.format(**a_dict)
		new_list.append(a_string)
	return new_list

string_factory(dicts, string)

