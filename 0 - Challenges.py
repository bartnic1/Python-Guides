# Section 1 Challenge:

# ipAddress = str(input("Please enter an IP address: "))
#
# segment_number = 1
# segment_length = 0
#
#
# if ipAddress == '':
#     print('There are no segments')
# else:
#     i = 0
#     for i in range(len(ipAddress)):
#         if ipAddress[i] == '.':
#             print('Segment {} is {} characters long'.format(segment_number, segment_length))
#             segment_length = 0
#             segment_number += 1
#         else:
#             segment_length += 1
#
#     if ipAddress[i] != '.':
#         print('Segment {} is {} characters long'.format(segment_number, segment_length))

# -------------------------------------------------------------------------------------------------------------------- #

# Section 2 Challenge:

# import random
#
# # Note, the randint function is inclusive of the lower and upper bounds.
#
# highest = 1000
# answer = random.randint(1, highest)
#
# guess = int(input("Please guess a number between 1 and {} (type 0 to exit): ".format(highest)))
#
# while guess != answer:
#     if 0 < guess > answer:
#         print("Please guess lower:")
#     elif 0 < guess < answer:
#         print("Please guess higher:")
#     elif guess == 0:
#         print("\nThanks for playing! The correct answer was {}".format(answer))
#         break
#     guess = int(input())
# else:
#     print("\nCongratulations, you have guessed the number correctly!")

# -------------------------------------------------------------------------------------------------------------------- #

# Section 3 Challenge A:

# menu = []
# menu.append(['egg', 'spam', 'bacon'])
# menu.append(['egg', 'sausage', 'bacon'])
# menu.append(['egg', 'spam'])
# menu.append(['egg', 'bacon', 'spam'])
# menu.append(['egg', 'bacon', 'sausage', 'spam'])
# menu.append(['spam', 'bacon', 'sausage', 'spam'])
# menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
# menu.append(['spam', 'egg', 'sausage', 'spam'])
#
# print('')
# print(menu)
#
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         for ingredient in meal:
#             print(ingredient)

# Section 3 Challenge B:

# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)

# Section 3 Challenge C: Tuples

# imelda = "\nMore Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# for i in range(len(imelda)):
#     if i != len(imelda) - 1:
#         print(imelda[i])
#     else:
#         for track in imelda[i]:
#             number, song = track
#             print("\tTrack Number: {}, Song Name: {}".format(number, song))

# For future reference, you can actually directly unpack the tuple in the for loop heading, by writing
# "number, song in imelda[i]", so that you use one less variable.

# -------------------------------------------------------------------------------------------------------------------- #

# Section 4 Challenge:

# print('\n')
# decimal = int(input("Please enter a decimal number no greater than 65535: "))
# p = int(input("Please enter a '2' for conversion to binary, or '8' for conversion to octal: "))
# copy = decimal
# final = []
#
# for i in range(15, -1, -1):
#     quotient = decimal//(p**i)
#     if quotient > 0:
#         final.append(quotient)
#         decimal %= p**i
#     else:
#         final.append(0)

# Here you can use the delete statement to remove leading zeros:


# if decimal == 0:
#     final = [0]
#
# i = 0
# if final != [0]:
#     while final[i] == 0:
#         del final[i]
#         i += 1

# Map: Apply a "function" to every item of "iterable" and return a list of the results.
# In this case, the join method joins each member of the list (the join(list) part) with an empty string '' between
# them.

# num = int(''.join(map(str, final)))
# if p == 2:
#     print("In binary, your number is: {}".format(num))
#     print("In comparison, Python converts {} to {:0b}".format(copy, copy))
# elif p == 8:
#     print("In octal, your number is: {}".format(num))
#     print("In comparison, Python converts {} to {:0o}".format(copy, copy))

# Remember in the future, that the print statement can include end = '' as a parameter, to avoid returning a new line
# each time! This way you can just print all the digits in one go without converting them.

# Also note that instead of using a list, you could have used an empty string '', and added to the string using the +=
# operator.

# a = ''
# a += 'test'
# a += ' more added on'
# print(a)

# Also note that you can perform bitwise operations using the ampersand operator (&).

# -------------------------------------------------------------------------------------------------------------------- #

# Section 5 Challenge A:

# Modify the program so that the exits are a dictionary rather than a list. The values should be the dictionaries
# holding the possible exits. Then create a dictionary that allows players to go in the direction of their choosing

# print('=' * 50)

# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in a forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# commands = {"WEST": "W",
#             "EAST": "E",
#             "NORTH": "N",
#             "SOUTH": "S",
#             "QUIT": "Q"}
#
# method_1 = False
# method_2 = False
#
# loc = 1
# while method_1:
#     availableExits = ", ".join(exits[loc].keys())
#     print(locations[loc])
#     if loc == 0:
#         break
#     direction = input("\nAvailable exits are " + availableExits + ". Where would you like to go? ").upper()
#     print()
#     if len(direction) > 1:
#         for command_word in commands:
#             if command_word in direction:
#                 direction = commands[command_word]
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction\n")

# Note that a more efficient way to complete this challenge, is to search the dictionary for the command the player
# typed, rather than going through all the commands and seeing if one of them exists in what the player typed. This way,
# even if your command list has hundreds of entries, you won't have to search through all of them; you only need to
# search through the 5-6 words the player typed!

# To do this, one uses the "split" command, which splits up a string into a list, partitioned by a delimiter you have
# entered (default is space). "string".split() for default, or "string".split(',') if you want to split by commas.

# while method_2:
#     availableExits = ", ".join(exits[loc].keys())
#     print(locations[loc])
#     if loc == 0:
#         break
#     direction = input("\nAvailable exits are " + availableExits + ". Where would you like to go? ").upper()
#     print()
#     if len(direction) > 1:
#         player_commands = direction.split()
#         for player_command_word in player_commands:
#             if player_command_word in commands:
#                 direction = commands[player_command_word]
#                 break
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction\n")

# Challenge 5B:

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in a forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# challenge5b = False
# loc = 1
#
# while challenge5b:
#     availableExits = ", ".join(locations[loc]["exits"].keys())
#     print(locations[loc]["desc"])
#     if loc == 0:
#         break
#     else:
#         allExits = locations[loc]["exits"].copy()
#         allExits.update(locations[loc]["namedExits"])
#     direction = input("Available exits are " + availableExits + ". Where would you like to go? ").upper()
#     print()
#     if len(direction) > 1:
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:
#                 direction = vocabulary[word]
#                 break
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction\n")

# -------------------------------------------------------------------------------------------------------------------- #

# Section 6, Input/Output Challenge:

# Modify the program from the Second Dictionary challenge of lecture 56
# to use shelves instead of dictionaries.
#
# Do this by creating two programs. cave_initialise.py should create the two
# shelves (locations and vocabulary) with the appropriate keys and values.
#
# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 45, everything
# before that (modified to use shelves) will be in cave_initialise.py.

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(locations[loc]["exits"].keys())
#
#     print(locations[loc]["desc"])
#
#     if loc == 0:
#         break
#     else:
#         allExits = locations[loc]["exits"].copy()
#         allExits.update(locations[loc]["namedExits"])
#
#     direction = input("Available exits are " + availableExits).upper()
#     print()
#
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:  # more than 1 letter, so check vocab
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:   # does it contain a word we know?
#                 direction = vocabulary[word]
#                 break
#
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")

# -------------------------------------------------------------------------------------------------------------------- #
#
# 7.1: Time Functions Challenge
#
# import time
#
# clocks = ["time", "perf_counter", "monotonic", "process_time"]
# print()
# for clock in clocks:
#     print(("For {}: ".format(clock) + str(time.get_clock_info(clock))), end='\n\n')
#
# print(time.time())

# 7.2: Datetime Functions Challenge

# import pytz
# import datetime
#
# print()
# all_timezones = {1: "Europe/Amsterdam",
#                  2: "Europe/Athens",
#                  3: "Europe/Berlin",
#                  4: "Europe/Brussels",
#                  5: "Europe/Helsinki",
#                  6: "Europe/Lisbon",
#                  7: "Europe/Luxembourg",
#                  8: "Europe/London",
#                  9: "Europe/Kiev"}
#
# for x in sorted(all_timezones):
#     print(str(x) + ': ' + all_timezones[x])
#
# # pytz.timezone() converts an appropriate string to a tz object. That object cna be used to find the date and time
# # local to that timezone using datetime.now. Additionally, UTC time is obtained using datetime.utcnow(), and together
# # with localize, creates both an aware UTC time (just the UTC time + 00:00) and an aware local time (+XX:YY with
# # respect to UTC time).
#
# tznum = 1
# while tznum != 0:
#     tznum = input("\nPlease enter a number to view the local time for that timezone. To escape, enter 0. "
#                   "To view the list of timezones, type L.\n")
#     while tznum not in list("0123456789"):
#         if tznum.upper() == 'L':
#             for x in sorted(all_timezones):
#                 print(str(x) + ': ' + all_timezones[x])
#             tznum = input("\nPlease enter a number to view the local time for that timezone. To escape, enter 0. "
#                           "To view the list of timezones, type L.\n")
#         else:
#             tznum = input("That entry is invalid. Please enter a number between 1-9. To escape, enter 0. To view the"
#                           "list of timezones, type L.\n")
#     if int(tznum) == 0:
#         break
#     tz_object = pytz.timezone(all_timezones[int(tznum)])
#
#     utc = datetime.datetime.utcnow()
#     aware_local = pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
#     timezone = datetime.datetime.now(tz=tz_object)
#
# # %A: Day of the week, %x: Day number, %X: Time, %z: Offset from UTC
#
#     print("Local to {}, the date and time is:\n{} {}."
#           .format(all_timezones[int(tznum)], timezone.strftime('%A %x %X %z'), timezone.tzname()))
#     print("\nIn your timezone, {}, the date and time is:\n{}."
#           .format(aware_local.tzname(), aware_local.strftime('%A %x %X')))
#     print("\nIn UTC, the date and time is:\n{}".format(utc.strftime('%A %x %X')))
#
# print("Program complete")

# -------------------------------------------------------------------------------------------------------------------- #

# import tkinter
#
# # Constant parameters
#
# mainPadding = 10
# valPadding = 1
# minWindowSizeX = 140
# minWindowSizeY = 180
#
# # Main Window initialization
#
# mainWindow = tkinter.Tk()
# mainWindow.geometry('640x480+500+300')
# mainWindow.title("Calculator")
# mainWindow['padx'] = mainPadding
# mainWindow['pady'] = mainPadding
#
# # Set column and row weights
#
# for i in range(4):
#     mainWindow.columnconfigure(i, weight=1)
# for i in range(6):
#     mainWindow.rowconfigure(i, weight=1)
#
# # Set Iterating Parameters
#
# buttonValues = ["C", "CE", 7, 8, 9, '+', 4, 5, 6, '-', 1, 2, 3, '*', 0, '=', '/']
# colCounter = 0
# rowCounter = 1
# colMax = 2
#
# # Button and Entry window generation. You can also create a list of lists; once a for loop completes the iteration
# # over one of the inner lists, it can be set to proceed to the next row using a greater for loop.
#
#
# tkinter.Entry(mainWindow).grid(row=0, column=0, columnspan=4, sticky='news', padx=valPadding, pady=valPadding)
#
# for val in buttonValues:
#     if colCounter >= colMax:
#         colMax = 4
#         colCounter = 0
#         rowCounter += 1
#     if val != '=':
#         tkinter.Button(mainWindow, text=str(val)).grid(row=rowCounter, column=colCounter, sticky='news',
#                                                        padx=valPadding, pady=valPadding)
#         colCounter += 1
#     else:
#         tkinter.Button(mainWindow, text=str(val)).grid(row=rowCounter, column=colCounter, sticky='news', columnspan=2,
#                                                        padx=valPadding, pady=valPadding)
#         colCounter += 2
#
# # One additional thing you can do is get the values of the keys after drawing them, and then use those to get the min
# # width and height. For this to work however, you would need to disable the initial geometry setting.
#
# # mainWindow.update()
# # mainWindow.minsize(width=mainWindow.winfo_width(), height=mainWindow.winfo_height())
#
# mainWindow.minsize(width=minWindowSizeX, height=minWindowSizeY)
# mainWindow.mainloop()

# -------------------------------------------------------------------------------------------------------------------- #

import tkinter

mainWindow = tkinter.Tk()

result_text = tkinter.StringVar()
result_text.set("Hello")
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

mainWindow.mainloop()



