***   Computation of Factorial      ***
***   First by Iteration(fact_Iter) ***
***   then by Recursion(fact_Recur) ***


def fact_Iter(n):
    """Assumes that n is a Factorial of an int>0"""
    result=1
    while n>1:
        result*=n
        n-=1
    return result
    

def fact_Recur(n):
    """Assumes n is a Factorial of an int>0"""
    if n==1:
        return n
    else:
        return n*fact_Recur(n-1)
        




