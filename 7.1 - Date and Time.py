# Here we first learn about importing modules. These allow you to use modules or functions created in other scripts.
# Turtle simulates the movement of a turtle with various commands, along with a graphical representation of that journey

# Time is a separate module. You can use the sleep method to freeze the program for "x" seconds (x is the parameter).

# import turtle
# import time

# Note you can also perform a more selective import, rather than importing the whole module:
# In this case however, you will no longer need to reference the turtle module, since you have imported the functions
# directly. Thus you can call forward, right and done without and decimal prefix:

# from turtle import forward, right, done

# Another way to import things, which is not recommended is to import (asterisk). This imports all the methods in turtle
# EXCEPT those that start with an underscore _. The reason why is because you may accidentally find that a function
# shares the same name as one of your variables or defined functions. If this is the case, depending on the order which
# you import your module and define your function/variable, one will overwrite the other.

# from turtle import *

# noinspection PyUnresolvedReferences

# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# time.sleep(4)

# Alternative:

# forward(150)
# right(250)
# forward(150)
# done()

# Note on the right, some warnings appear concerning the forward, right, etc. methods. This is a bug in intelliJ.
# To ignore these warnings, you can either write the line above turtle.forward, except that this only works for the
# proceeding line.

# A better way to do this is to click on the hovering light bulb whenever you see a squiggly line, and then click:
# "Mark all unresolved attributes of 'turtle' as ignored".

# If you wanted to see the warnings again, go to Analyze, Configure Current File Analysis, Configure Inspections, open
# the Python tab (note it is blue indicating a change), and then scroll down to see what has been changed.
# This will end up being "Unresolved references". If you click on that, you can then remove .turtle from the list
# using the minus sign (or add another with the plus).

# You can also use a special command in the turtle module to stop the program:

# turtle.done()

# Now you have to close the pop-up window explicitly to end the program (ordinarily, without done, it autocloses).

# -------------------------------------------------------------------------------------------------------------------- #

# The standard Python library includes a set of basic modules, including shelve and random, as well as built-in
# core modules that are called automatically. You can see these by using the dir() method (not the same as the dir
# command in command prompt).

# print(dir())

# Anything that starts with an underscore shouldn't be changed without good reason. There is no such thing as a private
# variable in Python, but underscores indicate intention. For two underscores, its not meant to be changed at all.

# In this case two underscores are used. The following shows the built in functions:

# print(dir(__builtins__))

# or:

# for m in dir(__builtins__):
#     print(m)

# You can also import a module such as shelve, and then examine its contents using dir(shelve).

# import shelve
#
# print(dir())
# print()
# print(dir(shelve))

# The shelve module has a Shelf class included. The close() method is a part of this class.

# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)

# Note some of the standard modules are written in C. These are usually used to provide direct access to system
# functionality, such as file I/O. But some are written in Python. To open these files in IntelliJ, hold control and
# click on the module in question to see all the code it contains.

# Another way to get more information is to use help(shelve). Be sure to check online documentation as well!

# help(shelve)

# You can also request help on individual functions:

# import random
#
# help(random.randint)

# ----------------------------------------------------------------------------------------------------------------------#

# One of the simplest modules in Python is the "webbrowser" module (new defaults to zero).

import webbrowser

# webbrowser.open("https://www.python.org/", new=1)

# The help function actually uses webbrowser to provide information on various modules.

# help(webbrowser)

# There you can learn about how to use various methods, such as the get method, which allows you to set a "controller"
# should be available, not sure why not. Here's an example using firefox:

browsing = False

if browsing:
    controller = webbrowser.get(using='C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s')
    controller.open("https://www.python.org/", new=1)

# After looking at the Q&A, you can get firefox working if you enter the path of the browser, and add a %s. This is a
# string formatter (recall from basics of python section) that passes a URL string for the program to open.

    print("test1 %s %s" % ('test2', "test3"))
# This will print "test1 test2 test3"

# You can also use webbrowser.register() in order to add new browsers for use by Python.
# Unfortunately, Tim Buchalka states that the documentation on this method is fairly poor. To get a better understanding
# of how to use the method, he recommends looking at the source code, but that it is too early in the course to do that.

# -------------------------------------------------------------------------------------------------------------------- #

# Time

# Localization refers to the time in any particular place, as well as the format used to represent dates in
# that particular location. The local time may depend on timezone as well as whether daylight savings is being used.

# For scientific and computer applications, its common to work with coordinated universal time or 'UTC'. Note that UTC
# is a compromise between english and french translations, so that's why the abbreviation isn't CUT. Its also known as
# zulu time.

# Dates and times in computer applications are commonly stored as UTC, together with an offset describing how many hours
# ahead or behind UTC they are. A flag indicates whether daylight savings time applies. Rather than using local time,
# it is recommended that you store your dates using UTC format to ensure readability for all users.

# Python provides three modules to deal with dates and times: Time, DateTime, and Counter.

# Its useful to read the documentation on time: https://docs.python.org/3/library/time.html

import time

# The epoch is the period of time following Jan. 1 1970 (may be different depending on your platform). To check, you can
# use time.gmtime(0):

print(time.gmtime(0))

# Local time gives the current time, complete with the tm_isdst boolean flag for daylight savings time.
print(time.localtime())

# time.time() prints the number of seconds since the start of the epoch.
print(time.time())

# Note that by entering time.time() as an argument into localtime(), it produces the same result.

# The output of gmtime() and localtime() is of the class 'time.struct_time'. This is known as a "named tuple", which
# can be created. Named tuples are just like ordinary tuples, but they also allow you to access components using a name:

time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

# from time import time as my_timer <-- First trial
# from time import perf_counter as my_timer <-- Second trial (same result)
# from time import monotonic as my_timer <-- Third trial (same)
from time import process_time as my_timer
import random

reaction_test = False

if reaction_test:
    input("Press enter to start ")
    wait_time = random.randint(1, 6)
    time.sleep(wait_time)
    start_time = my_timer()
    input("Press enter to stop\n")
    end_time = my_timer()

# strftime() converts the time.struct_time named tuple into a string format that is easily readable. The first
# parameter denotes the format (%X means "locale's appropriate time representation"), and the second is the struct_time.

    print("Started at: " + time.strftime("%X", time.localtime(start_time)))
    print("Ended at: " + time.strftime("%X", time.localtime(end_time)))

    print("Your reaction time was {} seconds".format(end_time - start_time))

# Note that there are some issues with the program above. If you press enter twice from the outset, once the second
# input line appears in the run window, it will instantly register that enter was pressed and log the end time.

# Another problem is that if the end time comes after daylight savings is applied, the reaction time might be an hour
# too late or too early.

# Lastly, the system clock could be changed while waiting for the player to press enter. Most computers keep their time
# synchronized with a time server on the local network, or over the internet. Occasionally if the system clock is too
# far ahead/behind, it may be set back/forward at inopportune times.

# You can use perf_counter to give an accurate measure of elapsed time. It is a very precise clock normally used to
# benchmark code. Note that this should not be used to give the local time, since it measures time starting
# from the point when the code was run. This is different from time.time(), since it gives the time since the beginning
# of the epoch in seconds.

# An additional timing function is "monotonic". The special feature of this function is that it can't go backwards. This
# rules out adjustments due to daylight savings, as well as to the computer's internal clock when it synchronizes with
# an external time server.

# The last timing function is "process_time", which records the time taken by the CPU to perform the calculation rather
# than the overall elapsed time. On your computer it prints a 0.0...maybe your CPU is too fast?

# Overall, if measuring elapsed time, it is recommended to use perf_counter. If dealing with real times, use the time
# function. Note that perf_counter and process_time are both monotonic, so its not clear what advantage monotonic has.

# For more info, see PEP (Python Enhancement Proposal) 0418.

# -------------------------------------------------------------------------------------------------------------------- #

#Date and Time

#import time

# It is preferable to use the date and time module if you are working with dates, even though the time module can handle
# both.

# To find your time zone, you can use time.tzname (this returns a tuple with the local non-DST timezone and the local
# DST timezone if applicable). You can use time.timezone to find the offset of the local (non-DST) timezone in seconds
# west of UTC.

# This means its positive in the US, zero in the UK, and negative in most of Europe.

# Tuple (Time zone, Daylight Savings (if applicable))
print(time.tzname)
# Scalar
print(time.timezone/3600)
# Boolean
print(time.daylight)

# This shows that, in Toronto, EST is UTC-5. If you remove daylight savings, ET is UTC-4. The same
# results are shown below when you call gmtime() for UTC time, and localtime() for local time.

# Also remember that daylight savings has to exist for the second string in the tzname tuple to make sense. To check
# whether your timezone uses daylight savings, check if time.daylight returns a "1".

# Below, %c represents the locale's appropriate date and time representation (see documentation for more formats)

print("The epoch on this system starts at: " + time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1} hours".format(time.tzname[0], time.timezone/3600))

# Next you can check if DST is in effect:

if time.daylight != 0:
    print("\tDaylight Savings Time is in effect in this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# Note for the abovestrftime() for local time or UTC, try not to use %z as it is depracated (see footnotes online).

# -------------------------------------------------------------------------------------------------------------------- #

# Using datetime:

# Aware objects are capable of locating themselves relative to other aware objects using time zone and daylight saving
# time information.

# Naive objects don't contain enough information to unambiguously do this. The program itself will have to specify
# whether the naive object represents UTC, or local time, or some other timezone.

# Date objects are naive, but datetime objects can be aware.

import datetime

# The datetime module defines a class called datetime. To access this, type datetime.datetime. Then within that class,
# you can call various methods, like today():

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# datetime.now() allows you to specify a timezone by inputting a tz object, but otherwise today() and now() both give
# local time while utcnow() gives utc.

# However, datetime.tzinfo is an abstract class. For now this means that the datetime.tzinfo object can't be created.

# Following from the last section, the pytz module was installed using pip3 (make sure to use pip3 over pip, since it
# is specifically meant to be used with Python 3. Using pip will install the module in Python 2).

# That module allows you to create a timezone object using pytz.timezone("string") where the string represents a region.

# To get more information on the pytz module, go to: http://pythonhosted.org/pytz/

import pytz
import datetime

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# The list of all possible timezone strings is given by the following:

for x in pytz.all_timezones:
    print(x)

# You can also get a list of countries by their abbreviation (key) and full name (value) by calling the country_names
# dictionary. Note that many timezones exist even for one country, so you can't enter these into the code above.

for x in sorted(pytz.country_names):
    print(x + ":" + pytz.country_names[x])

# The following code won't work, since the last dictionary won't necessarily use the same keys as country_names does
# (some countries aren't assigned a time zone! See Bouvet Island as an example.)

# for x in sorted(pytz.country_names):
#     print("{}:{}:{}".format(x, pytz.country_names[x], pytz.country_timezones[x]))

# The timezone database is maintained by the IANA (Internet Assigned Numbers Authority). Its also referred to as the
# Olsen database, after its creator (https://www.iana.org/time-zones). This is the definitive database that keeps
# records of timezone and daylight savings time information.

# In any case, to fix the error you can use the .get() command. That way if the dictionary doesn't find any value
# associated with a particular key, it won't return an error.

for x in sorted(pytz.country_names):
    print("{}:{}:{}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

# A more descriptive version of the above code, printing a custom message instead of "none" if no time zone is defined
# for a given country's key:

for x in sorted(pytz.country_names):
    print("{}:{}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        print(pytz.country_timezones(x))
    else:
        print("No time zone defined")

# In this more advanced code, you get a list of the country abbreviations from country_names, and using the
# pytz.country_names dictionary, you find the full country name corresponding to that abbreviation.
# Then, for that country, you create a sorted list of timezones. For each timezone, you create a datetime.tzinfo object
# and enter it into datetime.datetime.now() in order to retrieve the local time. Now you can print each zone and the
# local time in that zone, for each country. If no timezone exists, then the else statement prints the more descriptive
# message.

for x in sorted(pytz.country_names):
    print("{}:{}".format(x, pytz.country_names[x]), end=': \n')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones(x)):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

# Now so far, getting local time from universal time hasn't been too hard. Getting from local time to universal time
# requires that you also store time zone information, including DST. Generally it is recommended that you immediately
# convert local time to UTC once you get them.

# It turns out that using the localize function to convert naive local times to aware local times doesn't work so well!
# So instead the instructor says that we should use an alternate method, where you enter in the utc_time into the
# localize function, and then call the astimezone() method. By default, it will convert UTC to your local time

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

# Timestamps are seconds since the epoch

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

# Depending on your timezone, timestamp will be different, since it has to add or subtract a certain number of hours
# since that the epoch  at the greenwich line (or in the UTC "timezone")

s = 1445733000
t = s + (60*60)

# GB stands for great britain

gb = pytz.timezone('GB')

dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))

# However, even the previous two lines of code give incorrect values, because when you use the "fromtimestamp" function,
# the documentation states that it assumes you want to convert it into local time. So then the datetime, in local time,
# is converted into GB time. To fix this, the timestamp is first converted to UTC time, and then to local GB time:

dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))

# The result, 1:30 AM on October 25th, is the correct answer. Note that in the second case, after daylight savings time
# comes into effect, the local timezone relative to UTC changes as it should. Since GB is on the greenwich mean line,
# it goes back to normal "UTC zone" time, which is to say it has an offset of zero.

# In general the instructor recommends that coders use a virtual machine, set to a specific time zone, if handling code
# that requires timezone information to be used regularly. Next: A challenge.

# -------------------------------------------------------------------------------------------------------------------- #

