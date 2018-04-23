# From the intro, Python is an object oriented interpreted language. The object oriented aspect means it supports
# multiple inheritance, to be learned later.

# You can specify an index for a string, which will return the letter. [1:2] means you start at the second value
# (since python starts counting at zero), and ends before the third value (i.e. only one value is printed).
# The third index indicates how many characters are skipped. [::3} prints every third character in the string,
# starting at the first (zeroeth).

parrot = "Norwegian Blue"
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[::3])
print(numbers[-4])

# Using the 'in' operator to determine whether a string is present in another string (returns true or false)
days = "monday, tuesday, thursday, friday"
print('monday' in days)
print('monday, tue' in days)
print('month' in 'monthly donations are always accepted')

# str method, converts value in brackets to string
print("I have" + str(2) + "shovels in my shed")

# This is quite tedious if you have many numbers. Instead, it is preferable to use "replacement fields":
print('my shovel is in the {0}, together with my {1} {2}'.format('shed', 2, 'cows'))

# Using the string formatting operator % (deprecated in Python 3 (i.e. its not recommended to be used).
# It is used quite frequently, however, in Python 2).

# 'd' stands for integer, and 's' stands for string

age = 15
print('My age is %d years' % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

# With for loops. Note the %2d means you allocate two spaces for the answer.

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i*i, i**3))

# Additional specifiers. Before the decimal: Provide at least this many spaces.
# After the decimal: Provide this many (actual) decimal places, increasing allocated digit space dynamically

print('\nPi is approximately %20.1f' % (22/7))
print('Pi is approximately %12.10f' % (22/7))

# Now using replacement fields. Note we have added new features; the second index (after the colon) indicates how many
# spaces should be allocated for that replacement field. The less than sign indicates that it can be less than 4 if
# possible; this means that you get values that are aligned along the left hand side.

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

# Here 0 specifies the zeroeth value in the format list, 12 specifies the number of spaces allocated, and 50 specifies
# the number of decimal places desired (decimal places override the number of spaces allocated)

print('\nPi is approximately {0:12.50}'.format(22/7))

# One advantage of replacement fields, is that you can use values like {2} repeatedly; otherwise, with string formatting
# operators, you have to enter in the same value over and over again. Also...

print('If you only need to {} something {}, then you can just use empty braces'.format('specify', 'once'))

# Note that in this case, if you do want to reuse some replacement fields, you will need to enter a number

# There are two ways to extend a line vertically. Companies like google mandate an 80 character limit, so that code is
# readable on most computer screens without having to scroll horizontally. You can either use \ or () around your
# expression to continue it on the next line. As shown this works regardless of the type of expression you use:

a = 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+ \
    1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1
a = (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+
     1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)

random_string = "______________________ ______________________ ______________________ ______________________ " \
                "______________________ ______________________ ______________________ ______________________ "
random_string = ("______________________ ______________________ ______________________ ______________________ "
                 "______________________ ______________________ ______________________ ")

print('Value of a: ' + str(a))
print(random_string)