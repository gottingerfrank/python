# Comparison of a simple Countdown Function -
# first as an iterative Version,
# then as recursive Version ...



# Iterative Version of a Countdown Function
# (Also see recursive Version of Countdown Function!)

def countdown_iter(n):
    while n>=0:
        print n
        n-=1
    print 'Blastoff!'

# Recursive Version of a Countdown Function
# (from Book "Python - Think like a Computer Scientist")
# Also see iterative Version of Countdown Function!

def countdown_recur(n):
    if n<=0:
        print'Blastoff!'
    else:
        print n
        countdown_recur(n-1)
