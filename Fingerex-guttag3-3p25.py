#	*********************************
#	*********************************
#	*******	 edX MIT6.00.1x  ********
#	*******  Finger Exercise ********
#	*********************************
#	*********************************

#	Finger Exercise from Book: J.Guttag, Ch.3.3, p.25
#
#	Let s be a string that contains a sequence of decimal numbers(Floats)
#	separated by commas, e.g., s='1.23,2.4,3.123'.
#	Write a program that prints the sum of the numbers in s

# 	Program/method (Python 2.7) to compute sum of extracted floats from string s:

s=raw_input('Enter a String of Numbers separated by Kommas:')

def float_sum(s):
    total=0.0
    for f in s.split(','):
        subtotal=float(f)
        total=total+subtotal
    return total
# return value of function ...


print float_sum(s)
