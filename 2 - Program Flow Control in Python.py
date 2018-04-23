# Indenting: Note that one indent (or tab) is equivalent to 4 spaces. Try not to mix up spaces and tabs!

# Note the for look is calling the print method, which makes up the code block; everything with the same level
# of indentation is part of the same code block

# Also, you can select "reformat code" from the code drop-down menu at the top, which will clear up any errors or
# problematic spacing.

# Example:
for i in range(1, 12):
    print('No. {} squared is {} and cubed is {:<4}'.format(i, i ** 2, i ** 3))

# -------------------------------------------------------------------------------------------------------------------- #

# If: Runs indented code block if condition is met
# Elif: Runs indented code block if alternative condition is met (this is short for else if)
# Else: Runs indented code block if none of the previous conditions are met

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
#
if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print ("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print('You got it first time!')

# Better formatted version:

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time!")

# -------------------------------------------------------------------------------------------------------------------- #

# More complex else, elif conditions:

age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# True/false conditions. Note that there is no boolean data type, but by using the built-in boolean function, certain
# expressions can evaluate to true or false (in addition to typing in true/false explicitly).

# Also note that many empty statements are automatically evaluated as False without any boolean function (see below
# for an example where simply pressing return (no text entered) is equivalent to false.

x = False

print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

if x == bool([]):
    print('works')

# Cool things you can do with booleans:

x = input("Please enter some text: ")
if x:
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

# One last example using 'not'. Note, its often recommended to use brackets around the true/false condition for
# clarity, though its not necessary.

age = int(input("How old are you? "))
if not (age < 18):
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Come back in {0} years".format(18-age))

# -------------------------------------------------------------------------------------------------------------------- #

parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter in parrot:
    if letter in 'aeiou':
        print("Give me an {}, Bob".format(letter))
    else:
        print("give me a {}, Bob".format(letter))
else:
    print("I don't need that letter")

    # Note that you could also do it the other way, by typing in "if letter not in parrot:" etc.

# -------------------------------------------------------------------------------------------------------------------- #

# For loops:

# for i in "statement":
#     print('{}'.format(i))

number = "9,223,372,036,854,775,807"
cleanedNumber = ""

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]
        print('{}'.format(number[i]), end='')

newNumber = int(cleanedNumber)
print("\nThe number is {} ".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    # print("This parrot is " + state)
    print("this parrot is {}".format(state))

# -------------------------------------------------------------------------------------------------------------------- #

# Can use continue to bypass the remainder of a block of code, and move on to the next iteration of the for loop

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("I am ignoring " + item)
        continue
    print("Buy " + item)

# Note that break exits the for loop entirely:

for item in shopping_list:
    if item == "spam":
        print("I am ignoring " + item)
        break
    print("Buy " + item)

# Note this interesting example. If spam is found, it breaks out of the for loop, and since the 'if' statement was
# found to be true, then the else doesn't activate. Note that it can't refer to the third if statement, since the
# else precedes that statement and code must follow sequentially as the line number increases.

# Otherwise, if spam was not found, then the else statement activates.

# Aside: "Camel case" is the term used to describe variable casing done in the following way: nastyFoodItem.
# That is, the first letter is uncapitalized, while the first letters of every following word are capitalized, with
# no spaces between the words. Often these are good conventions to follow, and maintain throughout all your
# programming languages.

# Remember though, that Python variables are case sensitive!


meal = ["egg", "bacon", "spam", "sausages"]
# meal = ["egg", "bacon", "tomato", "sausages"]

nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it?")

# -------------------------------------------------------------------------------------------------------------------- #

# End of Section 2
