# Recursive Version of a Countdown Function
# (from Book "Python - Think like a Computer Scientist")
# Also see iterative Version of Countdown Function!

def countdown_recur(n):
    if n<=0:
        print'Blastoff!'
    else:
        print n
        countdown_recur(n-1)
        



    


