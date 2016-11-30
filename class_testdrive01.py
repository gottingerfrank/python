##################################################
###############    Experiment(s)   ###############
##################################################

class Animal(object):
    def __init__(self, skin, teeth, type, name):
        self.skin = skin
        self.teeth = teeth
        self.name = name


bear = Animal("furry", "sharp", "Bear", "Biggie")



print bear.teeth
print bear.name

pig = Animal("pinkish", "little", "Piglet", "Porcelino")

print "porco has", pig.skin, "skin","Hello! My Name is", pig.name

#   **
# ((--))
#  \vv/
#

print pig.name.upper()

