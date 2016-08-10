
def fact_Recur(n):
    """Assumes n is Int>0"""
    if n==1:
        return n
    else:
        return n*fact_Recur(n-1)
        

