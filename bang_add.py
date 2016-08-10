#   MITx 600.1x FingerExercise
#   Week 2 - Lecture 3 - L3 Problem 5
#   For-loop summing up a range of Integers up to
#   the Variable 'end', which is given
#   needs input variable 'end' - e.g:
#    end=6
#    end=-9


def bangAdd(end):
    """For a given Variable 'end' this function adds all
    values 1 through 'end', and prints out the result.
    Also added functionality for negative Integers"""
    end = int(end)
    x = 0
    if end >= 1:
        for i in range(1,end+1):
            x+=i
    else:
        for i in range(1,end-1,-1):
            x+=i
    print x
    return x


bangAdd(end)
