# Binary is a base two number system
# Low/high voltages are used in computers to simulate an on/off state. But in theory you can have ten voltage ranges
# that allow for a base 10 (decimal) system

# Decimal uses the digits 0-9, binary uses 0 and 1. For decimal:
# 1000 = 1*10^3 + 0*10^2 + 0*10^1 + 0*10^0
# For a binary based number system, this would be computed in the following way:
# 1000 = 1*2^9 + 1*2^8 + 1*2^7 + 1*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
# Thus, in binary, 1000 is represented as 1111101000.

# Note that in binary, each 1 or 0 is viewed as a "bit". 8 bits make a byte, 1024 bytes make a kilobyte. Higher
# values proceed in powers, so 1024^3 bytes makes a megabyte, 1024^6  bytes makes a gigabyte, and so on.

# Also note that a byte, consisting of 8 bits, can detail the value of digits fro 0 to 255 (so 256 in total). This is
# how RGB colours may be defined (although they also often use hexidecimal, or base 16 number systems).

# The code below right-aligns the first value, and right-aligns the second value by leaving space for 8 digits, while
# simultaneously filling in zeros for any of the first digits few that are not equal to 1. "b" indicates that teh number
# should be given in binary form.

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

# Three operations involving binary digits: OR, AND, and XALL (short for exclusive all). The OR operation sets each
# final bit in a binary number to 1 if either of the corresponding bits for the operands was 1 (and 0 otherwise).

# Thus, 00000100 or 00001000 yields 00001100. Similarly, 00001100 or 00001011 yields 00001111. In decimal, this is
# 4 or 8 giving 12, while 12 or 11 gives 15.

# For AND, each bit in the final answer is set to 1 if both bits in the operands are equal to 1. Hence,
# 00001100 and 00001000 gives 00001000 (or 12 and 8 gives 8), while 00001000 and 00000111 gives 00000000 (8 and 7 gives
# 0).

# So one can see that this is identical to the true/false interpretations of OR and AND statements normally used in
# Python, but it occurs for each individual bit in the byte.

# For XOR, the bit in the answer is 1 if either but not both of the corresponding bits in the operands is a 1.
# Hence, 00001100 XOR 00001000 = 00000100 (or 4), and 00000100 XOR 00000111 = 00000011 (or 3).

# Bytes explain why ASCII characters can not be used to represent all the languages around the world, as ASCII
# requires that all of the possible characters fit onto one byte of memory (meaning there are only 256 characters).

# Unicode resolves this by using two or four bytes per character, which allows many more characters to be represented.

# -------------------------------------------------------------------------------------------------------------------- #

# Now because binary takes so many bits to write out a large number, programmers prefer to use hexidecimal, which is
# base 16. Because base 16 is a power of 2, converting between binary and hex is easy. Decimal numbers from 0 - 255 can
# be written using only 2 hex digits!

# Hex numbers, from 0 to 15, are: 0-9 and then 0a, 0b, 0c, 0d, 0e, 0f for 10, 11, 12, 13, 14, 15 respectively. Note that
# each hex number can be represented by 4 bits, called a 'nibble'. An 8 bit byte can be represented with 4 hex digits.

for i in range(17):
    print("{0:>2} in hex is {0:>02x}".format(i))

# To differentiate hex numbers from decimals, Python allows programmers to use the 0x prefix:

x = 0x20
y = 0x0a
print(x)
print(y)
print(x*y)

# You can also do this with binary, using the 0b prefix. Also note that any leading zeros can be removed without
# affecting the printed result:

print(0b00101010)
print(0b101010)

# Also, you can use octal with "0o" prefix. Octal numbers can be used to represent file read/write permissions (1 = --x,
# 2 = -w-, etc. From the Python Masterclass, rw-r--r-- is a common read/write command that is written as 644 in octal,
# since 6 = rw- and 4 = r--.

print(0o123)
