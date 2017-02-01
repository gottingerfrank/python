#def disemvowel(word):
#    word = list(word)
#    for letter in word:
#        if letter.isalpha():
#            word.remove(letter)
#    word = "".join(word)
#    return word
#

def is_vowel(letter):
    if letter in "aeiouAEIOU":
        return True
    else:
        return False

def disemvowel(word):
    novowels = []
    for letter in word:
        if is_vowel(letter):
            continue
        else:
            novowels.append(letter)
    novowels = "".join(novowels)
    return novowels

print(disemvowel("HELLooh we are some hiedeous PEoPLE"))

