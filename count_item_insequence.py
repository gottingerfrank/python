##################################################
###############   Coding Exercise  ###############
##################################################

# Coding Exercise - Count function 
##################################################

def count(sequence, item):
    """"Returns the number of times an
    item occurs in a sequence"""
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

sequence = [1, 2, 3, 4, 5, 3, 3, 2]

print(count(sequence, 3))















##################################################
# END