##################################################
###############   Coding Exercise  ###############
##################################################

# Coding Exercise - Function to replace word in 
# sentence with "*"*len(word)
##################################################

def censor(text, word):
    text = text.split(" ")
    for s in range(len(text)):
        if text[s] == word:
            text[s] = len(word)*"*"
    text = " ".join(text)
    return text

# Example
text = "Hello I am here again, you fuckers"
word = "fuckers"

print(text)

text = censor(text, word)

print(text)














##################################################
# END