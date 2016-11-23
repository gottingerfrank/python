##################################################
###############   Coding Exercise  ###############
##################################################

##################################################
###		 Codecademy: Python Course(Python2)    ### 
### Dicts/Lists/for-loops - Part 2 - continued ###	
##################################################
##################################################


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def is_even(number):
    try:
        if number % 2 == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        return None

for number in a:
    if is_even(number):
        print number
    else:
        pass
        

##################################################
# END