# Dictionaries and sets are considered as unordered collections, which also guarantee no duplicates.

# Sets are similar to lists in that they are intended to store similar items. However, you can't access individual items
# using an index, since they are unordered.

# Dictionaries contain key valued pairs. The values are accessed by means of a key. Example:

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# Note the key is separated from its value by a colon. The key always comes before the value (to the left of the colon).

print(fruit)
print(fruit["lemon"])

print('='*50)

# Motorbike example - Note that you don't need to write definitions on new lines:

bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}

print(bike["engine_size"])
print(bike["colour"])

# One restriction on keys is that they must be immutable; hence you may use tuples, but not lists. Also note that the
# values may be any type of data, including other dictionaries or even mutable sets (tested).

# You can also add to dictionaries as seen below:

fruit["pear"] = "an oddly shaped apple"
print(fruit["pear"])

# Also note that keys are unique. If you assign a new value to an existing key, it replaces the old value. This is
# demonstrated below. As well, if "apple" were defined again *below* the original definition in the original dictionary,
# you would redefine apple.

fruit["pear"] = "great with tequila"

print(fruit["pear"])

# Now to remove entries, you can use the "del" command; but make sure you specify the key. If you type del fruit, you
# will delete the dictionary entirely.

# del fruit["lemon"]
# print(fruit)

# If you want to clear all the entries, do the following:

# fruit.clear()
# print(fruit)

# If you enter in a key that doesn't exist, you get a "key error":

# print(fruit["tomato"])

# Note you can also do:

for name, description in fruit.items():
    if description == "great with tequila":
        print(name)

# And use the following method to see all of your keys:

print(fruit.keys())

# You can use get to return a value for a specified key. Also the nice thing about get is it doesn't return an error if
# an invalid key is entered; it just returns the "None" string.

# Note that this is the default. To change the string use fruit.get(key, "message"). See below:

test = False
while test:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)

# Note also that the has_key() method is deprecated, so code like this won't work:

# dict_key = "grape"
# fruit.has_key(dict_key)

# Should be replaced with a "if dict_key in fruit" to test the True/False condition
# To iterate over the keys:

for snack in fruit:
    print(fruit[snack])

# The keys are connected to their values by one-way hash functions. In fact, usually the values are called 'hashes'.
# However working out what key was used to produce a hash can take a powerful computer months. This is useful in
# cryptography or calculating checksums (i.e. ensuring the file you download from the internet is the same as what was
# originally uploaded, by comparing the equality of the checksums).

# The items are organized in the dictionary in a particular order only when the dictionary is first created. Afterwards,
# calling the items maintains the same order. Note however that each time the dictionary is created, the order is
# random, due to how the keys are randomly assigned in the memory.

for i in range(3):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('='*40)

# Keep in mind that adding or deleting items from the dictionary will disturb this order, so its not something to rely
# on too much.

# It turns out that there are ordered dictionaries, to be discussed later when looking at libraries. If you did want to
# order a dictionary, its easiest to just form a list and then order that list. Below, fruit.keys() doesn't return the
# normal type of list which comes with a sort command, so generating a list is necessary:

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " - " + fruit[f])

# To make the code more concise, if ordered_keys isn't being used anywhere else, you can shorten the program. Note how,
# when using the sorted function, you can enter in fruit.keys() as a data type without running into the same problems
# as using the .sort() method, since it still behaves like a sequence.

print("\nShortened:")

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# If you don't care about sorting, you can shorten it further:

print("\nUnsorted")
for f in fruit:
    print(f + " - " + fruit[f])

# To get values:

for val in fruit.values():
    print(val)

# However note that this is very inefficient, and it is much better coding practise to use the keys. Also notice that
# fruit and fruit.keys() returns the same value for "key", though technically I think it would be better to use
# fruit.keys()

for key in fruit:
    print(fruit[key])

# Both fruit.keys() and fruit.values() are both list like objects, called view objects:

print(fruit.keys())
print(fruit.values())

# Below, see how even though the variable fruit_keys was not updated, because it is a view object, it changes based on
# whether or not the dictionary is updated.

fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

# Finally the fruit.items(), another view object,  method returns both the keys and values. Note that the sequence can
# be viewed as a tuple, and in fact converted into one using the tuple() function:

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

# You can then use this just like you've used other tuples:

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# Conversely, you can make a dictionary from tuples using the dict constructor:

print(dict(f_tuple))

# -------------------------------------------------------------------------------------------------------------------- #

print("="*50)

# Now going back to strings, recall that strings are in fact immutable. The join method takes a sequence and creates a
# new string from it. Below, this is not a good way of producing new strings as it is fairly inefficient, because every
# time it goes through the loop, it creates a new copy of newString. In this case, augmented assignment (+=) doesn't
# really help you since strings are immutable.

myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
newString = ''
for c in myList:
    newString += c + ", "

print(newString)

# Now use join. Observe that you can use this with a list, or a sequence (such as a string):

newString = ", ".join(myList)
print(newString)
newString = ", ".join(letters)
print(newString)
newString = ", ".join(fruit.keys())
print(newString)

print('='*50)

# You can use this new found knowledge to create a simple adventure game:
#              NORTH
#   (2)-<->- 5 Forest
#    |          |(2)
# 2 Hill <-- 1 Road <--> 3 Building
#    |          |(2)
#   (1)--<-- 4 Valley

# This map can be used to play a basic adventure game, using dictionaries. Note that "exits" must be used, as exit is
# a built-in command in python that closes the program!

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"}

# You can use a list of dictionaries, to detail the available options depending on the player's location:

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

game = False

loc = 1
while game:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    direction = input("\nAvailable exits are " + availableExits + ". Where would you like to go? ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

# See challenges for more on this example.

# Note that a more efficient way to complete this challenge, is to search the dictionary for the command the player
# typed, rather than going through all the commands and seeing if one of them exists in what the player typed.

# This makes use of the "split" command, which splits up a string into a list, partitioned by a delimiter you have
# entered. Example:

print(locations[0].split())
print(locations[3].split(","))
print(' '.join(locations[0].split()))
print('='*50+'\n')

# MORE ON DICTIONARIES:

# Recall our original fruit list. Lets add some veggies:

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have more fruit, please?"}
print(veg)

# Note that this method does not return a new dictionary, it just updates a pre-existing dictionary:

a = veg.update(fruit)
print(a)

# Actually printing veg will give you the updated dictionary:

print(veg)

# Now if you wanted to create a new combined dictionary, while leaving the old dictionaries as they were, its better to
# use the copy method:

print('='*50)
veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have more fruit, please?"}

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

# And the original dictionaries are the same as they were:

# print(veg)
# print(fruit)

# Now going back to the game, we can add in various locations to the dictionary:

print('='*50+'\n')

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "4": 4, "5": 5},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

commands = {"WEST": "W",
            "EAST": "E",
            "NORTH": "N",
            "SOUTH": "S",
            "QUIT": "Q",
            "ROAD": "1",
            "HILL": "2",
            "BUILDING": "3",
            "VALLEY": "4",
            "FOREST": "5"}

# Note: keys() on line 331 is redundant and can be removed

method_2 = False
loc = 1
while method_2:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])
    direction = input("\nAvailable exits are " + availableExits + ". Where would you like to go? ").upper()
    print()
    if len(direction) > 1:
        player_commands = direction.split()
        for player_command_word in player_commands:
            if player_command_word in commands:
                direction = commands[player_command_word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction\n")

# One advantage to using dictionaries over lists is that insertion and deletion of keys and their hashed values is
# extremely fast (although those operations aren't used here). However, the access by key is also extremely fast, so
# that would be useful for a game like this.

# Side note: When you iterate over a dictionary, python automatically uses the keys, so the extra call to use the
# method .keys() isn't actually necessary, as seen on line 331.

# -------------------------------------------------------------------------------------------------------------------- #

# SETS:

# In Python, sets are unordered and contain no duplicates, so they are similar to dictionaries. Unlike a dictionary,
# items aren't accessed via a key. Furthermore items in sets must be immutable objects. Also, sets support the
# intersection and union operations.

# You define a set using curly braces, only this time you don't need the colons defining any values for their respective
# keys. You can also use the set() function to generate a set. Below, a list is inserted as the argument.

# Also remember that test_set = {[1,2,3,4,5]} will return an error, as a list is mutable and thus can't be an element of
# a set (the actual error text reads " TypeError: unhashable type: 'list' ")

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print('='*50)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# Note that the order of all the animals in the sets changes, since they are inherently unordered.
# Also, observe that if you wanted to create an empty set, two curly braces {} won't do it, because that defaults to
# an empty dictionary rather than a set. Thus its better to do this by using the set function with an empty argument.

empty_set = set()
empty_set2 = {}
empty_set.add("a")
# empty_set2.add("a")

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# Using union: Note that the new set is ordered. Note that you could also do squares.union(even) and get the same result

print(even.union(squares))
print(len(even.union(squares)))

print("="*50)

# Using intersection. The ampersand (&) is a short form for using the .intersection method.

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

# Now to sort them, in order to more easily observe how they change when taking differences:

print(sorted(even))
print(sorted(squares))

# Note below, that the minus sign is a short form for using the .difference method. Its generally recommended to use the
# .difference() syntax, because it makes it clear that you are working with sets.

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

# More on items in a set (from Jean-Paul): Items in a set are stored in a hash table. The values in an object are used
# to calculate a hash value for each item (not necessarily unique). For example, one algorithm could assign a number
# for each letter in the alphabet (a = 1, b = 2, etc.), such that "Ian" has a value of the sum of those numbers, i.e.
# 24. Then the object Ian would have a hash value of 24; which would indicate where in the hash table you should look
# for Ian (Jean-Paul also referred to it as a bucket number in the hash table).

# Strictly speaking items only need to be hashable. If you have a name that can change, then the hash code would also
# change and you would not occupy the place originally assigned for your name in the table.

# As some extra content: <= and >= operators stand for "issubset" and "issuperset", while < and > are strict subsets or
# supersets. Hence {1} < {1} is false, but {1} <= {1} is true, as shown below:

print({1} <= {1})
print({1} >= {1})
print({1} < {1})
print({1} > {1})

# Also note that you can use the .update() method to add the contents of another set to an existing set. This is to be
# differentiated from .add(), which only adds a single element to a set. You can use update on any iterable, such as
# adding a list to a set.

# LAST VIDEO:

# You can also use the .difference_update() method to change an existing set (in this case, taking squares away from
# even).

print('='*50)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

# A symmetric difference is the opposite of an intersection; it gives you everything except the intersection aka the
# union minus the intersection. A quirk with Python is that squares.symmetric_difference(even) comes out sorted even
# if you didn't explicitly sorted. Don't rely on this though, or any other instances you note when using sets, as it
# may change in future updates (or if using older versions)

print("Symmetric even minus squares: ")
print(sorted(even.symmetric_difference(squares)))
print("Symmetric squares minus even: ")
print(sorted(squares.symmetric_difference(even)))

# Finally, you have symmetric_difference_update. This updates the set it was called upon, rather than generating a new
# set.

# To remove items from a set, you can either use .remove() or .discard(). The difference is that discard() shows no
# error if the item you are trying to remove does not exist in the set, while remove() does.

squares.discard(4)
squares.remove(16)

# Discard: No error, does nothing, since 8 isn't in the set
squares.discard(8)
print(squares)

# Remove: Shows error
# squares.remove(8)

# Sometimes this is useful when you want to detect an error, and do some processing depending on which error type it is.
# Try and except are useful in this case, and will be discussed further later on in the course.

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")

# The same is true when accessing keys in a dictionary using dictionary[key] as opposed to dictionary.get(key) to obtain
# the value. The former will return an error, while the later handles the exception on its own.

# Now about supersets and subsets: (this is >= or <=)

even = set(range(0, 40, 2))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print('even is a superset of squares')

if {1}.issubset({1}):
    print('yes')

# Lastly, the frozen set. This means the set can't be changed by using any add, remove or discard methods.

even = frozenset(range(0, 100, 2))
print(even)

# So methods like the add method will only return an error:
# even.add(3)

# Other than that, you can use the same old intersection and union operations that all sets have. The only thing you
# can't do is use any of the update methods, since that would change the frozen set.

# Python documentation has a good overview of everything learned so far at the following recommended link:
# https://docs.python.org/2/library/sets.html

# Python 3 has similar documentation, but it isn't laid out in a nice table as it is for the Python 2 page.

# Now its time for the final challenge.
