# There are three steps to reading files in Python. Using the built-in open(), you open the file, then you read the
# file (either line by line or as a whole block), and then you close the file using the .close() method applied to your
# file variable.

# Note that it is particularly important to close the file if you write to it, as if you don't it may get corrupted,
# in which case not all data can be written to the file.

# Make sure to specify whether you want to read or write to your file, by specifying the mode after entering the file
# directory. 'r' stands for 'read only'.

# Note that on Mac and Linux, folders are specified using a forward slash. On windows, you use a backslash. Since some
# commands are specified with backslashes, such as \n or \t, it is useful to either put an r before the quotation marks,
# indicating it should be read as raw text, or to separate each folder by a double backslash \\. However "r" is intended
# only for regular expressions. If you are instead specifying a directory that ends in \, your program will fail.

# On the forums, Jean-Paul actually recommends using forward slashes, as Python will happily cope with the change.

# If you enter in an incorrect directory, the console in IntelliJ will actually tell you which folder it is searching
# in. You can use this to modify the searched directory by going up or down a folder using ../ or ./ (forgot which).

# Below: If you specify end='' for your print function, it will not print a new line character at the end. Since new
# line characters exist in the text document itself, its unnecessary to add such a character explicitly.

jabber = open("C:\\Users\sw0rd\OneDrive\Python Tests\sample.txt", 'r')
for line in jabber:
    # print(line, end='')
    if "jabberwock" in line.lower():
        print(line, end='')
jabber.close()

# A more pythonic, and safer way to open files (which removes the risk of failing to close them), is to use the with
# statement, which tidies everything up once the object it is applied to is no longer needed. Not below that 'as' allows
# you to define the variable jabber with open(...):

with open("C:\\Users\sw0rd\OneDrive\Python Tests\sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

# If you used the first method (prevalent in Python 2.x), you would have to close the file using the .close() method.
# A potential issue with this is that if an error occurred along the way, the file may fail to close.

# Due to this, most programs have to prepare for errors to ensure that files still close even if an error occurs. Using
# the with statement, you don't need to worry about an error preventing the closing of a file. Otherwise, you need
# to use a form of error handling, to be discussed later.

print('='*50)

# Now to use the .readline(), .readlines(), and .read() methods:

# Another way to read a file is through a while loop. So long as line = jabber.readline() is not empty, the while
# statement defaults to true, until it reaches the end of the poem and an empty string for that line. Also, the
# .readline() method will automatically move on to the next line every time it is called, so you don't need to iterate
# over any kind of list.

with open("C:\\Users\sw0rd\OneDrive\Python Tests\sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# As another example, the .readlines() method produces a list of lines of the entire file, complete with newline
# characters. Note you could also change lines to lines[::-1] to reverse the sequencing of those lines:

with open("C:\\Users\sw0rd\OneDrive\Python Tests\sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

# You can also use the .read() method. Instead of creating a list of lines, it actually reads in the whole block of text
# as a single string. The lines[::-1] then creates the same string backwards, and so reverses all the words and the
# ordering of the lines in the poem.

with open("C:\\Users\sw0rd\OneDrive\Python Tests\sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines[0])
for line in lines[::-1]:
    print(line, end='')

# In summary: readline() returns a single string, and subsequent calls to this method returns following line in the file
# readlines() returns a list of strings, which is more memory intensive.
# read() returns a single string of the whole document, which is also more memory intensive.

# readline() is basically the same as using for line in "filename" (jabber in this case).

# read() also accepts an optional parameter specifying how much data to read. This will be covered later.

# -------------------------------------------------------------------------------------------------------------------- #

# Writing to a file:

# This time, when opening an object, you specify 'w' in order to write to a file. Also, now the print function can be
# used to print an entry of a list to another file:

# On Laptop: C:\Users\sw0rd\IdeaProjects\Masterclass is the stored directory
# On PC: C:\Users\Piotr\Desktop\Python Tests is the stored directory


cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file, flush=True)

print('done')


# Note that if you rerun this code, it will overwrite the previously existing file in the same directory. Also the
# = sign in file=city_file isn't actually an assignment operation, its actually used to provide a named argument in
# place of the file parameter. In this case, its frowned upon to put spaces before and after the equals sign.

# As an aside, the print function also has a "flush" argument that can be set to true or false (false by default).
# External devices (such as your computer monitor) have information transferred to them more slowly than the information
# is processed in the memory. So what happens is the information is first passed to a buffer, and then that buffer's
# data is transferred to the screen in the background.

# Additionally (from stack overflow) writing data can be costly, especially if you write one byte of code at a time. So
# a common way to improve performance is to write the data to a temporary buffer, so that once there is a lot of data,
# it is then written to the file. Thus by writing large blocks in one go, rather than many smaller blocks, your
# performance improves.

# Flushing the buffer basically clears the buffer by outputting all of the data that is in it. The ability to control
# when the buffer is flushed is important enough that Python 3 allows you to have direct control over it.  Also, note
# that the buffer is always flushed when python closes a file (so when filename.close() is used).

# -------------------------------------------------------------------------------------------------------------------- #

# Below we verify that we have properly outputted the file. Note the use of the .strip() method to remove certain text
# characters from each line in city_file:

cities = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

# More on strip: This method only removes specified characters from the beginning or end of a string:

print("Adelaide".strip("A"))

# Even if its only a partial match, it will still strip the end two characters:

print("Adelaide".strip("del"))

# -------------------------------------------------------------------------------------------------------------------- #

# Sometimes after writing to a file, it is difficult to read it back in the same format. So in this case, you may be
# able to write a tuple out to a file, but reading it back is difficult because it is read as a single string. However,
# Python does have the eval function that can be used to help here:

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
        contents = imelda_file.readline()
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for track in tracks:
    print(track)

# Note that eval is a security risk, in that if the code you are reading contains damaging instructions, Python will
# run it anyway.

# -------------------------------------------------------------------------------------------------------------------- #

# You can also append to a text file using the 'a' mode. This adds data to the end of a text file. So far, the three
# modes discussed are short for "rt", "wt", and "at", where "t" refers to a text file. They can also be specified the
# other way aroudn ("tr", "tw", and "ta"). This is because "t" is the default mode.

# The following link contains more information:
# https://docs.python.org/3/library/functions.html#open

# -------------------------------------------------------------------------------------------------------------------- #

# Reading and writing binary files in Python.

# This is useful if processing binary data (like an image file), or if you want to store variables in data.
# This time, you specify 'b' for binary. If you want to store strings, you must first convert to binary.

# "bw" is used to write to a binary file. This time you can use the write method instead of print, and the bytes
# function. The purpose of this function is to convert an integer into a binary value, in order to allow the program to
# write to bin_file. Notice you are passing a list to this function!

with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

# bytes() returns a bytes object, which is an immutable version of a byte array, to be looked at later.
# This is just a sequence of integers in the range of 0 - 255, or a sequence of bytes.

# Binary files can not be read as text files! If you try to read the outputted file in text format, you will just see
# a bunch of weird symbols. On the console however, the \ means its a character code, and x09 is actually equivalent to
# a tab character (t), while x0a is equivalent to a new line character (n). IntelliJ is thus doing an autoconversion.

with open("binary", "br") as binFile:
    for b in binFile:
        print(b)

# Note that the bytes() function works strangely. If you pass an integer to it, it creates a bytes sequence with that
# integer number of bytes all set to zero. By enclosing the integer in square brackets, you pasa a list with a single
# item i, which the bytes function converts to a single byte. If it fails to convert, you get an error.

# Note that you don't actually need to send each value i to the bin_file separately using an iterative approach. You
# can also pass the range as a whole. Thus the following code produces the same results as above:

with open("binary", "bw") as bin_file:
    bin_file.write(bytes(range(17)))

# The integer object also has a method to convert to bytes. Recall each byte, 8 bits is 2^8 = 256 numbers. This is
# the same as FF in hexidecimal. So FF FF stands for two bytes worth of data, and so on. It is customary when using
# binary to use an even number of bytes, so even though c only needed 3 bytes, 4 were used.

# "Big indian" stores the biggest byte first. "Little indian" stores the smallest byte first.

a = 65534       #FF FE
b = 65535       #FF FF
c = 65536       #00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

# Now to read the stored data, with e, f, g, h, i respective to a, b, c, x(big), and x(little):
# Notice that reading the last file in big indian format misreads the binary data, since it is reading
# the stored bytes differently.

with open("binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    f = int.from_bytes(bin_file.read(2), 'big')
    g = int.from_bytes(bin_file.read(4), 'big')
    h = int.from_bytes(bin_file.read(4), 'big')
    i = int.from_bytes(bin_file.read(4), 'big')
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)

# -------------------------------------------------------------------------------------------------------------------- #

# These are fairly simple ways to work with binary data. Python offers more advanced methods, using pickle and shelf.
# There is a process of saving data in another file format to be retrieved later; in java this is done through a process
# called serialization. In python, the process is called pickling.

# When an object is pickled, it is converted into a format that contains the objects data together with sufficient
# information for the object to be recreated when it is read from.

# Previously, it has been shown how numbers can be converted to bytes, and then stored as binary files. But in that
# process, it is difficult to imagine how more complex objects, such as a locations dictionary, can be stored.

# Using pickle, saving objects with complex structures is easy. First, you have to import the pickle library:

import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish Town Waltz')))

# Then, using the 'write to binary' format, use pickle.dump(target_object, variable representing object to write to).
# Note that the format that it writes in is specific to Python; opening it as a text file returns a lot of strange
# characters.

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# Now you can try reading using the pickle.load(variable representing previously written object) method.

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

# Once you open a file for writing, you can pickle as many objects as you want to to that same file. However, they
# must be read back in the same order that they were written:

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('='*40)

for i in even_list:
    print(i)

print('='*40)

for i in odd_list:
    print(i)

print('='*40)

print(x)

# There are very few objects in Python that can not be saved by pickling.  Now when you are pickling data, you can
# choose from one of five different serializing protocols. The latest protocol, is version 4 (from Python 3.4). The
# protocols aren't backwards compatible with earlier python versions however, so you won't be able to unpickle data
# from those versions.

# The first protocol was actually human readable; i.e. you could see the serialized data. To see this, you can type in
# protocol=0 as the third variable in pickle.dump(). Note that the values in imelda.pickle have 'L' characters used as
# delimiters.

# Protocol 1 is the first binary protocol. All versions of python should be able to unpickle data with that protocol.
# Python 2.3 introduced Protocol 2, which pickles classes more efficiently. However it also had a number of security
# checks removed, and was declared insecure. Thus it is not recommended for use.

# The first Python 3 protocol, protocol 3, is the default protocol used. All versions of Python 3 can understand data
# pickled using protocol 3, but data pickled won't be readable using Python 2.x (x being any number).

# Note that you can even use different protocols for each data dump, within the same file, as shown above. This is
# because python remembers which protocol was used for each data dump.

# You should generally only unpickle data that you trust! Example of bad code below:

# EXAMPLE:
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")

# del is the delete command; it removes the imelda.pickle file. Far worse effects are possible! And this happened just
# by loading a file.

# For more info, visit: https://docs.python.org/3/library/pickle.html

# -------------------------------------------------------------------------------------------------------------------- #

# The downside of pickling is that the data has to be stored in the computer's memory. For a large dictionary, this may
# not be a realistic option. The alternative option in Python is the "shelf" option. It is like a dictionary, except
# it is stored as a file in your hard disk rather than in memory.

# It differs from a dictionary in that the keys must be strings, rather than generic immutable objects such as tuples,
# but all the methods used with dictionaries can be used with shelf objects. Note that loading a shelf can also execute
# unwanted code, so the same security warnings apply.

# Below you don't need to specify read or write, it uses one or the other where appropriate. Basically, you write
# to fruit using the dictionary commands, and read it just as you would any other dictionary. Note you can write, read,
# and then write to your shelf all in the same with statement.

import shelve

with shelve.open('Shelftest') as fruit:
    fruit['orange'] = 'a sweet, orange citrus fruit'
    fruit['apple'] = 'good for making cider'
    fruit['lemon'] = 'a sour, yellow citrus fruit'
    fruit['grape'] = 'a small, sweet fruit growing in bunches'
    fruit['lime'] = 'a sour, green citrus fruit'

    print(fruit["lemon"])
    print(fruit["grape"])

# As you can see, shelftest is stored as a database file. The actual values are pickled, so it can store complex data
# structures. Also, shelves can not be initialized with a literal structure. So the normal dictionary initialization of:

# {"orange": "a sweet, orange citrus fruit"} would not be added to the shelf; instead a generic dictionary would be
# created that is accessible after the loop is closed, meaning it was not stored as a file.

# Remember that you can always do this manually. Side note: To remove indents from several lines at once, highlight them
# all and press shift+tab.

fruit = shelve.open('Shelftest')
fruit['pear'] = 'an oddly shaped, green fruit similar to an apple in texture'
fruit.close()

# -------------------------------------------------------------------------------------------------------------------- #

# Another example:

import shelve

with shelve.open('bike2') as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    del bike["engin_size"]

    for key in bike:
        print(key)

# Above, recall that when cycling through "bike", it assumes the user wants to look through the keys. So calling
# bike.keys() is unnecessary. Just like a dictionary, you can remove unwanted entries using the del command.
#
    print('='*40)

    print(bike["engine_size"])
    print(bike["engin_size"])
    print(bike["colour"])

# Shelves are persisted in files. So if you make a typo in "engine_size", for example, it will create a dictionary key
# and value for that. If you later change it, the same file will now have two entries, one that is correctly spelled and
# one that is incorrectly spelled. You can iterate through the entries though, to remove the one you don't want (see
# above).

# -------------------------------------------------------------------------------------------------------------------- #

# To avoid the errors you get from calling keys that don't exist, you can use the get method. This is the same as what
# you used with dictionaries.
# Just like a dictionary, you can add statements telling the user that their entry doesn't exist using a personalized
# string.

fruit = shelve.open('Shelftest')

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)
fruit.close()

# To rename all variables, right click on one of them, go to refactor, then click rename.

check = False

while check:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break

    if dict_key in fruit:
        description = fruit.get(dict_key, "We don't have a " + dict_key)
        print(description)
    else:
        print("We don't have a "+dict_key)
fruit.close()

# Just like a dictionary, the keys are unsorted, and actually have no defined order in general.

fruit = shelve.open('Shelftest')

ordered_keys = list(fruit.keys())
ordered_keys.sort()
ordered_keys = sorted(ordered_keys)

for f in ordered_keys:
    print(f + ' - ' + fruit[f])

# Because its coming from a database, on some systems they get autosorted alphabetically. However this is unreliable.
# To sort you need to turn the keys into a list, and then used the sort() method or the sorted() function.

fruit = shelve.open('Shelftest')

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())
print(fruit.keys())

fruit.close()

# Previously, in dictionaries and sets, the .values() method returned dict_values, while .items() returned dict_items,
# and similarly for .keys(). With shelves, you get something similar, called ValuesView, ItemsView, and finally KeysView
# respectively. For both dictionaries and shelves, these are all view objects.

# Being view objects, they don't change themselves, but do reflect changes in the underlying dictionary, or in this case
# the underlying shelf.

# -------------------------------------------------------------------------------------------------------------------- #

# Now, Tim discusses how to update a shelf and ways to increase performance. The example below uses the persistence
# of shelves as well as lists to represent multiple values for certain keys.

import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup

    # Won't work:

    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    # Will work:

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    # Will also work, so long as you set writeback to True:

    recipes["soup"].append("croutons")

    # Won't work if sync is directly after recipes["soup"] assignment, since sync removes all cached data, including
    # the list. Note that updating the soup list updates the values in the recipe, since they are view objects!

    recipes["soup"] = soup
    soup.append("cream")
    recipes.sync()

    for snack in recipes:
        print(snack, recipes[snack])
        recipes.sync()

# Note from above that the append method does not work as you would expect; i.e. you can not add an item to a list after
# obtaining its value with a key. The reason why is that the shelf has no way to know that the lists have changed. The
# appended items were only added to a copy of the recipes, but there is no trigger to have shelve write that data to
# recipes.dat. This is done to minimize disk access.

# You can also set writeback to true. In this mode, all entries accessed are also cached in the memory, and written to
# disk upon using the sync() or close() methods. The downside is heavier memory usage. Note you can only use sync()
# if writeback is enabled.

# The way it was used above however, won't work. When you sync, it writes all the data to disk, then starts caching
# again. So if something you access is no longer in the cache (which it won't be, immediately after a sync) then it's
# read from disk.

# If you move recipes.sync() after the append, then everything will work again.

# The side benefit of shelving is that you don't need to use SQL (structured query language) in order to extract data
# from a database. You can simply use normal python syntax. But a possible downside is that, because the data is pickled
# before being stored, the pickling procedure itself may require more processing power. Also if moving shelves between
# systems, the database may not work properly in the new environment.

# One more example, converting a dictionary to a shelf:

books = shelve.open("book")

# If defining a dictionary:

books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_on_toast": ["beans", "bread"],
                     "scrambled eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]},
        "maintenance": {"stuck": ["oil"],
                     "loose": ["gaffer tape"]}}

# If defining a shelf:

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])
print(books["maintenance"]["loose"])

books.close()

# See challenges.py.

