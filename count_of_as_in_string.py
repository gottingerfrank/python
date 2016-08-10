test_str=raw_input ("Please enter a string with a chose number of a's here:")
total=0
for i in test_str:
    if i=='a':
        total+=1
if total !=0:
    print total
else:
    print "There are no a's present in this string"