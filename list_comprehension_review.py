# Use a list comprehension to create a list, 
# threes_and_fives, that consists only of the numbers 
# between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.

# threes_and_fives = [x % 3 == 0 or x % 5 == 0 for x in range(1, 16)]

# threes_and_fives = [x % 3 or x % 5 for x in range(1, 16)]

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

print(threes_and_fives)

# --------------------------------

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
