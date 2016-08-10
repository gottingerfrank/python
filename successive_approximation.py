#   Code to find the Square-root of a number x
#   runs by iteration and using Floats to slowly
#   approximate the current guess to the Square-root of x

#   *** NOTE - been messing aroun a bit since original implementation ***

x=36
epsilon=0.001
step=0.0001
guess=0.0

while guess <= x:
    if abs(guess**2 - x) < epsilon:
        break
    else:
        guess+=step
        print guess
    
if abs(guess**2 - x) > epsilon:
    print'Failed'
    print 'Last guess was:',guess,'(for x = '+ str(x)+')'
    
elif abs(guess**2 - x) <= epsilon:
    print 'Succeded:'+' The Squareroot of the number x = '+ str(x)+' is:'
    print str(guess)
    
if int(guess)**2 == x:
    print 'Succeded: We have a perfect Square-root of x: '+ int(x)
    


