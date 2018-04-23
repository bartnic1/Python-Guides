# Lecture 1: Intro to Lists, Ranges, and Tuples

# A string is one type of sequence - STR

# Python has 6 additional built-in sequence types. 3 to be discussed here are lists, ranges, and tuples.
# The remaining 3 are binary sequence types, to be discussed in future sections.

# A list is a a sequence of things; they could be strings, numbers, classes, etc.
# Thus a list can be a list of lists!
# See online documentation (python's website) for an explanation on common sequence operations

ip_address = "123.23.235.89.09"
print(ip_address.count('.'))
print(ip_address.index('.'))
print('index: ' + str(ip_address.index('2', 0, len(ip_address)))) # Note; returns exception if string not found
print("find: " + str(ip_address.find('2'))) #Returns -1 if string not found



parrot_list = ["non pinin'", "no more", "a stiff", "bereft of life"]
parrot_list.append("a Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

# Can make a list with numbers:

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Note that numbers.sort() can only be interpreted as method that acts on numbers' it doesn't actually
# represent a new list. That is numbers.sort() can't be printed (in the console, it returns 'None'). In this case,
# the method returns 'none' bu the object itself is updated.

# To be learned later: Methods act on objects, which are instances of classes. They implicitly pass the information
# from their parent object into a function defined under the class. Functions are more general; they can optionally
# return some value, and they can accept a range of variables as arguments.

numbers = even + odd
numbers.sort()
print(numbers)

# Or, you could use the sorted function, built-in to python:

numbers = even + odd
numbers_in_order = sorted(numbers)
print(numbers_in_order)

# Note that order matters in lists - numbers and numbers_in_order are different lists.

# -------------------------------------------------------------------------------------------------------------------- #
# Lecture 2: More about lists

# You can use "list constructors", as a type of function to call in order to create lists
# Note that print is in fact a function, and when you pass a string to it, that is called a parameter.
# Frequently, 'argument' and 'parameters' are used interchangeably.

List_1 = []
List_2 = list()

# Note, they are the same (can also prove using == check).

print("List 1: {}".format(List_1))
print("List 2: {}".format(List_2))

# Here we have called the list() function with no parameters. But it can also be called with a single iterable parameter
# An iterable parameter is a parameter whose members can be called one at a time. Note all sequence types are iterable.

print(list('the lists are equal'))

# When you assign two variables to the same list, sorting that list will affect both variables as seen below:

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print("Same list: " + str(even))

# However, if you create a new list and assign it to another_even, we find that they are independent:
# Note the list constructor does not create a list within a one-member list, but rather a 4 member list as desired:

even = [2, 4, 6, 8]
another_even = list(even)
another_even.sort(reverse=True)
print("Independent: " + str(even))

# An important distinction here is that the contents of these lists are equal, but they don't point to the same
# variable in the memory. So in the first case print(another_even is even) would return True, but in the second example,
# print(another_even is even) would return False. However, in the second example, another_even == even would still be
# true (as it would in the first case), assuming you sort the another_even list.

print("")
another_even.sort()
print(another_even is even)
print(another_even == even)

# An easier way to declare a reversed list is to use a function, rather than declaring the list and then using a method:

print('')
even = [2, 4, 6, 8]
another_even = sorted(even, reverse=True)
print(another_even == even)

# Concatenating lists:

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)
numbers = even + odd
print(numbers)
numbers.append(5)
print(numbers)

# Mini-challenge question:
# More complex example. Note that you are appending lists to a master list here.

menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

print('')
print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)

# -------------------------------------------------------------------------------------------------------------------- #

# Every time you iterate over an iterable object (such as a list, or string), an iterator is created for that object,
# and your looping method uses that iterator to move through each each element of that object.

# When there are no more items, the iterator returns an error. So when you are using a for loop, it actually handles
# the error and terminates. We can actually create an iterable object explicitly, rather than implcitly by using a for
# loop, by using the iter function.

print('\nIterators')
string = '01234567890'

my_iterator = iter(string)
print(my_iterator)

# Now to go through each element (if you go too far, you get an error). This is exactly what a for loop does. Note this
# will help to produce iterable classes later on:

print(next(my_iterator))
print(next(my_iterator))

# Thus, these two statements are actually identical, since python creates an iterable automatically:

for char in string:
    print(char)

for char in iter(string):
    print(char)

# Mini-challenge!

print('\nMini-challenge\n')

items = [1, 2, 3, 4, 5]
iterable = iter(items)

for i in range(len(items)):
    print(next(iterable))

# Now time to talk about ranges! In python 3, its a built-in type of data. In Python 2, it was a function.

print(type(range(100)))
print(range(100))

# As seen, these are useful to iterate over, or to generate lists:

my_list = list(range(10))
print(my_list)

# More advanced usage. First index is the start, second is the end, last is the step size. Note it does not include
# the end number in the range. In Python, range is extremely efficient. range(10) and range(1000) use the same amount of
# memory!

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

# Ranges represent sequences that follow a defined pattern, and don't support many of the operations that normal
# sequences do (like concatenating strings, or using the multiplication operator to repeat a range). Thus
# 2*range(10) returns an error

# Using indexes:

my_string = 'abcdefghijklmnopqrstuvwxyz'
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0,10)

# By leaving the first and second entries in [::2] empty, you are slicing the whole array as itself. The last number
# only indicates that the range increases by 2:

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

# Additional example:

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('='*40)

# Note that range(0, 5, 2) == range(0, 6, 2) returns True, because they return the same elements
# Also note that taking slices of ranges, with a negative step size, actually reverses the range:

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

r = range(0,10)
for i in r[::-1]:
    print(i)

print('='*50)
# -------------------------------------------------------------------------------------------------------------------- #

# Tuples: Tuples are an ordered set of data. The difference between tuples and lists, is that tuples are immutable - or
# that they can't be changed. Tuples do not necessarily need to be enclosed in parentheses, but when printed, if they
# are a tuple, they will have parentheses. Below, only the first and third examples are tuples because of
# the syntactic ambiguity in the second example (after print(t)).

t = "a", "b", "c"
print(t)

# Note below, there is syntactic ambiguity. In order to specify that you want to print a tuple, you must enclose the
# sequence of characters with a set of parentheses (otherwise, you are just using the print function to print 3 char's).

print("a", "b", "c")
print(("a", "b", "c"))

# In general it is recommended to use brackets when defining tuples for clarity. Note in the example below, tuples can
# support numerous data types, which you can individually call using square brackets as with lists:

metallica = "Ride the lightning", "Metallica", 1984
print(metallica[0])
print(metallica[1])
print(metallica[2])

# But item assignment, such as metallica[0] = "Master of Puppets" returns an error as expected. However, tuples do
# support indexing and slicing, and you can use this to reassign your variable entirely:

metallica = (metallica[0], "Super Thunder", metallica[2])
print(metallica)

# Note that expressions on the right hand side of variable assignment are always evaluated before the left hand side is.
# In this way, you can update the variables. So to summarize, the object that the variable points to is immutable if it
# is a tuple, but the variable itself can be reassigned to a new object of the same type (or a new type entirely).

# Why use tuples? If you are using a dictionary key, you will need an immutable object. Also lists are generally
# intended to contain objects of the same type - they are said to be homogeneous. Tuples are intended to hold
# heterogeneous items, like strings and numbers.

# Tuples are also useful to ensure your code isn't changing accidentally. For example, in an adventure game, one would
# want the layout of the rooms to be fixed. The data for this layout could then be stored as a tuple.

# Now, will consider new ways to assign variables:
print('='*50)
a = b = c = d = 15
a, b = 12, 13
print(c)
print(a, b)
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))

# By "unpacking the tuple", you can easily assign tuple values to multiple variables:

imelda = "More Mayhem", "Imilda May", 2011
title, artist, year = imelda
print(title)
print(artist)
print(year)

# Below, it is important to put brackets around the pairings of song titles and their track number, because otherwise
# the Python interpreter will treat them as a single tuple consisting of 8 items, and any relation between the track and
# its number is not clear to the computer.

imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3,"Mayhem"), (4,"Kentish Town Waltz")
)

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

# You can also extract each track individually this way:

print('='*50)

imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), \
         (4, "Kentish Town Waltz")

title, artist, year, track1, track2, track3, track4 = imelda
print(track1)
print(track2)
print(track3)
print(track4)

# The limitation with this method is that you must name each variable, and if you miss one or have too many, then you
# will get an error or the print functions won't return anything. To finish off the section see challenges.

# In the challenge solution video, its also useful to note that if you have a list is an element of a tuple, then that
# list has mutable elements, and so you can effectively alter the tuple by changing the contents of the list (say, by
# appending new items to it).

# To learn about named tuples, see the date and time section.
