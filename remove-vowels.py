##################################################
###############   Coding Exercise  ###############
##################################################

# Coding Exercise - remove all vowels from string
##################################################

def anti_vowel(text):
    """Remove all vowels contained in the
    string 'text'"""
    vowels = "aeiou"
    result = []
    for letter in text:
        if letter.lower() not in vowels:
            result.append(letter)
    result = "".join(result)
    return result



##################################################
# END