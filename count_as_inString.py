#   ###########################################################
#   ## Finger-Exercise from edX online-course 600.1x by MITx ##
#   ###########################################################

#   Define String 's' to be searched for no. of a's:

s=raw_input("Please enter a couple of letters to define String s:\n\n")
print "\n"

#   Function 'count_as_in(s)' for the search mechanism:

def count_as_in(s):
    """Program to determine the Number (Count) of 'a's in String s.
    Finger Exercise from edX 600.1x online CS course by MIT"""
    
    total=0
    for i in s:
        if i=='a':
            total+=1
    if total !=0:
        print total
    else:
        print "There are no a's present in this string"


#   Call Function to initialise and begin search:

count_as_in(s)





