# Bitwise Operations in Python - part of Python/Advanced Topics
# ----------------------------------------------------------------

b3 = 0b11

b7 = 0b111

print(b3,b7)

# the bin() function transfers a number to a binary (base-2) string! 
bfunct1 = bin(765)

print(bfunct1)

# the oct() function transfers a number to a octary (base-8) string! 

octfunct1 = oct(765)

print(octfunct1)

# the hex() function transfers a number to a hexadecimal (base-16) string! 

hexfunct1 = hex(765)

print(hexfunct1)

# ----------------------------------------------------------------

# print numbers 0 through 5 in binary, using the bin() function

print bin(1)

print bin(2)

print bin(3)

print bin(4)

print bin(5)

# ----------------------------------------------------------------

# the int() function can also convert a number, given as a string together with
# the numbers base into a decimal number : e.g. int("10",2) --> 2 (int, in decimal)
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

# ----------------------------------------------------------------

# Note that you can only do bitwise operations on an integer!
# Trying to do them on strings or floats will result in nonsensical output!

shift_right = 0b1100
shift_left = 0b1

# Your code here!

shift_right = 0b011
shift_left = 0b100

print(bin(shift_right))
print(bin(shift_left))

# ----------------------------------------------------------------

number = 0b1110 | 0b101

# 0b1110
# 0b0101 (bitwise | (or)) =
# 0b1111

decnum = bin(0b1111)

print(decnum)

# ----------------------------------------------------------------

number = 0b1110^0b101

# 0b1110
# 0b0101 ^(bitwise XOR!) =
# 0b1011 = 11

print bin(number)
print int("1011",2)

# ----------------------------------------------------------------

# Bitwise NOT Operator (~): "Add one to the number and make negative""

print ~1
print ~2
print ~3
print ~42
print ~123

# ----------------------------------------------------------------
# Create Bitmask with Bitwise & (And) Operation, Function:

def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    return "off"
    
# ----------------------------------------------------------------

# Using the bitwise | operator will turn a corresponding bit on if it is off
# and leave it on if it is already on

a = 0b10111011
mask = 0b100

desired = a | mask

print bin(desired)

# ----------------------------------------------------------------

# Using the XOR (^) operator is very useful for flipping bits.
# Using ^ on a bit with the number one will return a result where that bit is flipped.

a = 0b11101110
mask = 0b11111111

number = a^mask
print bin(number)

# ----------------------------------------------------------------

# Finally, you can also use the left shift (<<) and right shift (>>) operators
# to slide masks into place

def flip_bit(number, n):
    mask = (0b1 << (n-1))
    result = number ^ mask
    return bin(result)

# Note: e.g: to flip the "n-th bit", we need to move over n-1 bits from the 1st bit...

# --- EOF ---
# ----------------------------------------------------------------
