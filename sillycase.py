# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"

def sillycase(string):
    first_half = string[:(len(string)//2)+1]
    second_half = string[(len(string)//2)+1:]
    string = first_half.lower()+second_half.upper()
    print (string)
    return string

