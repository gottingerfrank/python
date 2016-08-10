# counts number of a's in string (s)

s=type(str)
def count_a_in(s):
    total=0
    for i in s:
        if i=='a':
            total+=1
        if total !=0:
            return total
        else:
            print "There are no a's present in string (s)"
            
            