##################################################
###############   Coding Exercise  ###############
##################################################

# Coding Exercise - Function Add Digits
##################################################

def digit_sum(x):
    '''Takes in a positive int n and
    returns the sum of its digits'''
    total = 0
    for digit in str(x):
        total += int(digit)
    return total

##################################################
# END