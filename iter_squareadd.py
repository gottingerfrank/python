#    Program to calculate a number x**2 (X squared) by
#    successive addition of x...

#    Iterative() implementation


#    Base case: If x=0, then x**2=1, which means x=x**2 
#    Recursive case: x**2=x+((x-1)*x)
#    ans=x**2 (what we are looking for)   

def iterSquareAdd(x):
    squared=0
    X=x
    if x==0:
        squared=1
    else:
        while X!=0:
            squared+=x
            X-=1
    return squared
    
    
        
        



    

    


