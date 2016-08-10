#   MITx 600.1x FingerExercise
#   Week 2 - Lecture 3 - L3 Problem 5
#   For-loop summing up for given 
#   Variable 'end' is given

#   Written as function
#   needs input variable 'end' - e.g:

#    end=6

def bangAdd(end):
    """For a given Variable 'end' this function adds all
    values 1 through 'end', and prints out the result"""
    x=0
    for i in range(1,end+1):
        x+=i
    print x
    return x

bangAdd(end)







