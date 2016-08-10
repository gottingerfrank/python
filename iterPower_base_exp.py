def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=base
    iter = 1
    while iter < exp:
        iter+=1
        result = result*base
    return result
    
    