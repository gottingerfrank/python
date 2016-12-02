##################################################
###############   Coding Exercise  ###############
##################################################

# Codecademy: Python Course(Python2) 
# Classes - Test Drive (Test part2)

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
        
hippo = Animal("Berta", 45)

print (hippo.description())







##################################################
# END