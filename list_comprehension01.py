# ------------------------------------------------
# --------------  Coding Exercise  ---------------
# ------------------------------------------------

# Coding Exercise - Python: List Comprehension
# ------------------------------------------------

# List of squares evenly divisible by 2
even_squares = [x**2 for x in range(1,11) if (x**2) % 2 == 0]

print(even_squares)

# List of cubes evenly divisible by 4
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]

print(cubes_by_four)

# print odd list elements using slicing+step
my_list = range(1, 11) # List of numbers 1 - 10

print(my_list[::2])

# reverse list using slicing+step
my_list = range(1, 11)

backwards = my_list[::-1]

# reverse count from 0-100 in 10s/step:10 (as a list)
to_one_hundred = range(101)

backwards_by_tens = [x for x in to_one_hundred[::-10]]

print(backwards_by_tens)

# final exercise - list comprehension and slicing

to_21 = [x for x in range(1,22)]

odds = to_21[::2]

middle_third = to_21[7:14]

# ------------------------------------------------
# END