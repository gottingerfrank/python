

def fact_Iter(n):
    """Assumes that n is Int>0"""
    result=1
    while n>1:
        result*=n
        n-=1
    return result
    
    
 
def fact_Recur(n):
	"""Assumes that n is Int>0"""
	if n  == 1:
		result = n
	else:
		result = n * fact_Recur(n-1)
	return result







		
