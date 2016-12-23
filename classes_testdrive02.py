##################################################
###############   Coding Exercise  ###############
##################################################
# Classes - Test Drive (Test part2) (Python 3)   #
##################################################

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):   
        print (self.name)
        print (self.age)
    def health(self):
        if self.is_alive:
            return('Health is good')
        else:
            return('Not looking good...')

hippo = Animal("Berta", 45)

if hippo.is_alive:
    print('The fact that Hippo is alive is True !')
print (hippo.description())

print(hippo.health())

sloth = Animal("fattycatty", 8)
ocelot = Animal("graybeauty", 3)

print(hippo.health)
print(sloth.health)
print(ocelot.health)


##################################################
# END