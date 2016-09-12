def dict_invert(d):
    '''
     d: dict
    Returns an inverted dictionary according to the instructions above
    '''
#    "key" = d1
#    "value" = d2

#    Example: d = {1:10, 2:20, 3:30}
#    dict((d2,[d1].sorted())

#    Dictionary by name of d is given ...


    key_ls = d.keys()
    key_clean = []
                            
#   remove duplicates from unordered list of key-values (keys)

    for i in d.keys():
    	if i not in key_ls:
            key_clean.append()

#   Reverse/Inverse dictionary and order list:

    d_inverse = dict((d2, key_clean.sort()) for key_clean, d2 in d.iteritems())

    return d_inverse
