##################################################
###############   Coding Exercise  ###############
##################################################

# Codecademy: Python Course(Python2) 
# A Day at the Supermarket

##################################################
 
 
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

##################################################

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key], "\n"

##################################################

total = 0

for key in prices:
    item_rev = prices[key] * stock[key]
    print str(key) + ":", item_rev
    total += item_rev

print total

##################################################

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# create function to calculate bill from item list passed in
def compute_bill(food):
	total = 0
	for item in food:
		total += prices[item]
	return total

print compute_bill(shopping_list)

##################################################

# extended compute_bill function taking stock into account
def compute_bill(food):
	total = 0
	for item in food:
	    if item in stock and \
	    stock[item] > 0:
		    total += prices[item]
		    stock[item] -= 1
	return total
 

##################################################
# END