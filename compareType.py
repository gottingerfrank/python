varA=-5.44
varB='-4.2'

if type(varA) == str or type(varB) == str:
    print 'string involved'
else:
    if varA > varB:
        print 'bigger'
    if varA == varB:
        print 'equal'
    if varA < varB:
        print 'smaller'
        
