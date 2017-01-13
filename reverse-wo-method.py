##################################################
###############   Coding Exercise  ###############
##################################################

# Coding Exercise - reverse function without method
##################################################

def reverse(text):
    """Reverse the letters in the string 'text'
    without using the method .reverse()"""
    letters = []
    for letter in range(len(text)-1, -1, -1):
        letters.append(text[letter])
    reverse = "".join(letters)
    return reverse

text = "rabbithole"

print reverse(text)








##################################################
# END