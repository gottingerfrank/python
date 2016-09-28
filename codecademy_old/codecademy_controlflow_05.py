#	*********************************
#	********* codecademy ************
#	********* Exercises	 ************
#	*********************************

# Make sure that the_flying_circus() returns True


def the_flying_circus(x):
    if x>=15 or x<=10:
        print 'the circus artist is flying past the fire, evading it!'
    	if x>=15:
    		print'...he saltos twice far above the fire, landing savely on his feet'
    	elif x<=10:
    		print'...he flies too low, not making a great jump, but dodging the fire'
    elif x==15:
        print 'the circus artist touches the fire, but barely makes it over'          
    else:
        print 'the circus artist slips during the jump.He crashes into the fire!'
        
the_flying_circus(15)

