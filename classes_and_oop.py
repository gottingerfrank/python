# ------------------------------------------------
# --------------  Coding Exercise  ---------------
# ------------------------------------------------

# Classes and OOP - Introduction to Classes
# ------------------------------------------------

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


print(lemon.color)
print(lemon.name)
print(lemon.flavor)
print(lemon.poisonous)

print("-------------------------------------------")
# ------------------------------------------------

class Animal(object):
    pass

print(type(Animal))
help(Animal)

# Class Syntax
# ------------------------------------------------

# We started our class definition off with an odd-looking function: __init__()
# This function is required for classes, and it's used to initialize the objects it creates
# __init__() always takes at least one argument, self, that refers to the object being created
# You can think of __init__() as the function that "boots up" each object the class creates

class Animal(object):
    def __init__(self):
        pass

# ------------------------------------------------

# So far, __init__() only takes one parameter: self. This is a Python convention.
# It's overwhelmingly common to use self as the first parameter in __init__(),
# so we should stick to this convention.

# self is the first parameter passed to __init__()
# Python will use the first parameter that __init__() receives
# to refer to the object being created; this is why it's often called self,
# since this parameter gives the object being created its identity

class Animal(object):
    def __init__(self, name):
        self.name = name

# name refers to the created object's name by typing self.name = name

bird = Animal("birdie")  # Instantiating the class 'Animal' with a name of 'birdie'

print(bird.name)

bird.number = int(0b1011001)

print(help(bird))
print(bird.number)

print(type(Animal))
print(type(bird))

print("-------------------------------------------")
# ------------------------------------------------

# We can access attributes of our objects using dot notation
# e.g. instantiate new object with: >> zebra = Animal("Jeffrey") <<
# access attributes with dot.notation: >> zebra.name <<

class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
zebra2 = Animal("Billy")

print(zebra.name)
print(zebra2.name)

print("-------------------------------------------")
# Class definition
# ------------------------------------------------

# As mentioned, you can think of __init__() as the method 
# that "boots up" a class' instance object:
# the init bit is short for "initialize."

# The first argument __init__() gets is used to refer to the instance object,
# and by convention, that argument is called self

# If you add additional arguments—for instance, a name and age for your animal—setting
# each of those equal to self.name and self.age in the body of __init__() will make it so that
# when you create an instance object of your Animal class,
# you need to give each instance a name and an age,
# and those will be associated with the particular instance you create.

class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

print("-------------------------------------------")
# Scope
# ------------------------------------------------

# Another important aspect of Python classes is scope.
# The scope of a variable is the context in which it's visible to the program.

# When dealing with classes, you can have variables that are available everywhere (global variables),
# variables that are only available to members of a certain class (member variables),
# and variables that are only available to particular instances of a class (instance variables).

# The same goes for functions(/methods): some are available everywhere,
# some are only available to members of a certain class,
# and still others are only available to particular instance objects.

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)

# NOTE: each individual animal gets its own name and age
# (since they're all initialized individually),
# but they all have access to the member variable is_alive,
# since they're all members of the Animal class

print("-------------------------------------------")
# Methods
# ------------------------------------------------

# When a class has its own functions, those functions are called methods.
# You've already seen one such method: __init__().
# But you can also define your own methods!

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("berta", 7)

hippo.description()

print("-------------------------------------------")
# Member variables
# ------------------------------------------------

# A class can have any number of member variables.
# These are variables that are available to all members of a class.

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def description(self):   
        print(self.name)
        print(self.age)
        

hippo = Animal("Jake", 12)
hippo.is_alive = False

print(hippo.description)
print(hippo.is_alive)

sloth = Animal("Slothie", 5)
ocelot = Animal("Ocie", 4)

print(hippo.health)
print(sloth.health)
print(ocelot.health)

ocelot.health = "poor"

print(hippo.health)
print(sloth.health)
print(ocelot.health)

print("-------------------------------------------")
# More likely Class-Names
# ------------------------------------------------

# classes and objects are often used to model real-world objects.
# The code in the editor is a more realistic demonstration of the
# kind of classes and objects you might find in commercial software

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

my_cart = ShoppingCart("myself")

my_cart.add_item("macbook13", 1599)

print("-------------------------------------------")
# Inheritance
# ------------------------------------------------

# Inheritance is the process by which one class
# takes on the attributes and methods of another,
# and it's used to express an is-a relationship.

# For example:
# a Panda is a bear -
# so a Panda class could inherit from a Bear class.
# However, a Toyota is not a Tractor,
# so it shouldn't inherit from the Tractor class.
# (even if they have a lot of attributes and methods in common)

# Instead, both Toyota and Tractor could ultimately
# inherit from the same Vehicle class.

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

print("-------------------------------------------")
# ...
# ------------------------------------------------

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    "Makes triangles. A subclass of Shape"
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

una = Shape(3)    
threeoh = Triangle(2, 2, 3)

print(threeoh.side1)
print(threeoh.side3)


# threeoh.number_of_sides = 3
threeoh.area = 6

print(una.number_of_sides)
print(threeoh.area)
type(threeoh.area)

print(help(threeoh))

print("-------------------------------------------")
# Super-calls
# ------------------------------------------------

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee("milton")

print(milton.full_time_wage(10))

# ...
# ------------------------------------------------

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
    number_of_sides = 3

duo = Triangle(60,70,50)
print(duo.number_of_sides)

print("-------------------------------------------")
# ...
# ------------------------------------------------

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
    number_of_sides = 3
    
my_triangle = Triangle(90, 30, 60)

print(my_triangle.number_of_sides())
print(my_triangle.check_angles()())

print("-------------------------------------------")
# ...
# ------------------------------------------------

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
    number_of_sides = 3
    
my_triangle = Triangle(90, 30, 60)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


# EOF
# ------------------------------------------------