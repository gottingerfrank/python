# ----------------------------------------------------------------

squares = [x**2 for x in range(1,11)]

filter(lambda x: x >= 30 and x <= 70, squares)

print(filter(lambda x: x>=30 and x<=70, squares))

# ----------------------------------------------------------------

movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())

# ----------------------------------------------------------------

# Use a list comprehension to create a list,
# threes_and_fives, that consists only of the numbers
# between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.

# threes_and_fives = [x % 3 == 0 or x % 5 == 0 for x in range(1, 16)]

# threes_and_fives = [x % 3 or x % 5 for x in range(1, 16)]

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

print(threes_and_fives)

# ----------------------------------------------------------------

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]

print(message)

# ----------------------------------------------------------------

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)

print(message)

# --- EOF ---
# ----------------------------------------------------------------
