##################################################
###############   Coding Exercise  ###############


# Codecademy: Python Course(Python2) 
# Student becomes the Teacher

##################################################


# create 3 dicts: lloyd, alice, tyler

# give each dict the keys: "name", "homework", "quizzes" 
# and "tests"

lloyd = {"name": "Lloyd", "homework": [], "quizzes": [], "tests": []}

alice = {"name": "Alice", "homework": [], "quizzes": [], "tests": []}

tyler = {"name": "Tyler", "homework": [], "quizzes": [], "tests": []}

##################################################

# Fill in grades for lloyd (and other students - was done already)

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0,90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

##################################################

# create a list containing all three students (their dicts, being variables!)

students = [lloyd, alice, tyler]

##################################################

# for each student in the list students, print out his values for:
# name, homework, quizzes and tests - each item on a new line respectively

for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]

##################################################
# END
