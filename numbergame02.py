##################################################
###############   Coding Exercise  ###############
##################################################
# Loops - while/else-loop constructs Python 2.7  #
##################################################

# Number Game 2

from random import randint

random_number = randint(1, 10)

guesses_left = 3


while guesses_left > 0:
    guess = int(raw_input('Enter a number from 1-10> '))
    if guess == random_number:
        print'You win!'
        break
    else:
        print'That was not it.'
        guesses_left -= 1
else:
    print'You loose.'


##################################################
# END