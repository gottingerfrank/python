
def fact_Iter(n):
    """Assumes that n is Int>0"""
    result=1
    while n>1:
        result*=n
        n-=1
    return result
    
    