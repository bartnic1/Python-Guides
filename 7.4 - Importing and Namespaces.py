import blackjack
import os

testing1 = False
testing2 = False

if testing1:
    print(__name__)

# When you import a module, the code is loaded into memory and then executed. This is why importing blackjack as it was
# written in the course causes it to automatically run (i.e. without the if __name__ == __main__ condition).

# However, it also defines various namespaces. When read from a script, standard input, or from an interactive
# prompt, a module's '__name__' is set to '__main__'. This means that the module is running in the main scope.
# So in other words, if you run blackjack.py as the main program, the __name__ will be set to __main__.

# However, if you were to import Blackjack as a module (i.e. blackjack.py), then its __name__ will be set to
# the name of the module (i.e. blackjack), because the module is no longer the main program. That is, it is set to the
# filename without path or extension.

# This can be used to ensure that the code only runs when you explicitly call it.

if testing1:
    blackjack.play()

# Naming conventions:

# name_:

# From the date and time lesson, from_ and to were used to describe a range of dates in the date and time spinbox. The
# reason why from_ was used and not from, is because from already reserved as a keyword in Python.

# In cases where it seems logical to use the same word, but for a different function, the conventional way to rename
# the keyword is to place an underscore at the end. Hence, from becomes from_.

# _name:

# Unlike other languages, Python has no private or protected variables. But by convention, starting a name with an
# underscore indicates that it should be treated as protected; that is, its not intended to be used outside of the
# module where it is defined. Thus, it makes sense to refactor the name of _deal_card to _deal_card. Note that
# intelliJ will warn you whenever you try to use a protected function, as show below:

    # blackjack._deal_card(blackjack.cards)

# Another implication is that, if you type "from blackjack import *", everything that starts with an underscore is not
# imported. Recall that it is not advised to use import * statements, because its difficult to keep track of which names
# belong to your script, and which belong to the module you are importing. Thus you would call blackjack.new_game()
# instead of new_game(), possibly confusing it with one of your functions.

# globals() returns the dictionary containing the current scope's global variables:
    g = sorted(globals())

    for x in g:
        print(x)

# Note that if you use "from blackjack import *" at the top, then all the functions and variables will count as globals,
# except for those which start with an underscore, which won't be imported as discussed above.

# __name__

# Anything with two underscores before and after the name should not be changed, though they can be used.

# _ and __

# Anything labelled "_" or "__" are typically used as throwaway variables.

# Recursive functions:

# Recursive functions are functions that call themselves. .
# Example: Factorials


def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    """n! can also be defined as n * (n-1)!. This is a recursive function."""
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# Second example: Fibonacci sequence


def fib(n):
    """F(n) = F(n-1) + F(n-2). This is a very inefficient and slow method for numbers above 36!"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    """This runs significantly faster than the recursive function"""
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(2, n + 1):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

# Using either fact, factorial, fib, or fibonacci:
if testing1:
    for i in range(36):
        print(i, fibonacci(i))

    listing = os.walk('.')
    for root, directories, files in listing:
        print('\n\t'+root)
        for d in directories:
            print(d, end='\t')
        for file in files:
            print('\n'+file, end='')

if testing2:
    def list_directories(s):
        def dir_list(d):
            nonlocal tab_stop
            files = os.listdir(d)
            for f in files:
                current_dir = os.path.join(d, f)
                if os.path.isdir(current_dir):
                    print('\t'*tab_stop + "Directory " + f)
                    tab_stop += 1
                    dir_list(current_dir)
                    tab_stop -= 1
                else:
                    print('\t'*tab_stop + f)

        tab_stop = 0
        if os.path.exists(s):
            print("Directory listing of " + s)
            dir_list(s)
        else:
            print(s + " does not exist")

# Note that if you were to define tab_stop as global, then an error would appear because Python is expecting to find
# the variable declared (at least, defined with a value at most) in the outermost scope which is the Python file itself.

# While you can also solve the problem by amending the function to accept tab_stop as an additional parameter, the fix
# used in this case is to declare tab_stop as a nonlocal variable. This tells Python to search for the definition in
# one of the enclosing scopes of the main Python file (i.e. either the first enclosing function, or the one above that,
# and so on). Note that it won't search in the area with the same scope, since it is nonlocal.

# Another important fact about the nonlocal keyword is that the variables must exist in an enclosing scope; unlike
# with global, you can't create new variables from a local scope. This is because Python doesn't know which enclosing
# scope to use otherwise.

# As for some of the functions used:
# os.path.join function simply combines the path of the starting directory with the new filename, while os.path.isdir()
# checks whether the (now combined) path references a directory or just a single file.

# Note that '.' simply means that Python will list the directories present within the same folder that the current file
# is located (i.e. C:\Users\Piotr\Desktop\Python Tests)

    list_directories('.')

# The only things that create scope in Python are modules, functions, and classes.

# Another example on creating nested functions. Note that the variables in the innermost function are not available
# at a greater scope, but the variables in the outermost scope are available to all enclosed scopes, so long as you
# don't define them, in which case you would shadow the variables in the greater scope (and you would need to declare
# them using the nonlocal keyword).

# Side note: Variables introduced in if, while, or for loops are treated as having global scope if they are not within
# any other function or class.


def spam1():
    def spam2():
        def spam3():
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z
        y = " more " + x
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y
    x = "spam"
    x += spam2()
    # x = "spam" + spam2()
    print("in spam1, locals are {}".format(locals()))
    return x
print(spam1())

# There are 3 main things you want to try to do with functions:
# 1. Try to make them use only local variables, rather than nonlocal or global ones.
# 2. Think carefully before making seemingly trivial changes to code you're modifying. As seen above,
# changing x += spam2() to x = "spam" + spam2() breaks the code, since spam2() requires x, which is not yet defined.
# 3. Make sure you comment your code in instances like these, to help other coders know where subtle modifications can
# break the code.

# Also note that the locals are the same as the globals in the module scope:

if locals() == globals():
    print("Equal")

# Next, observe that when you write z += y as in spam3(), when printing the locals(), it shows y. This is due to
# optimization on the part of Python, where it adds nonlocal variables to the local namespace so that it doesn't have
# to hunt through a number of enclosing scopes every time it needs to reference that variable.

# In reality, y is still a nonlocal variable.

# The order in which Python searches for names: LEGB, or "Local Enclosing Global Built-Ins"
# Enclosing refers to non-local or free variables. Free variables are variables that are used in a scope where it is
# not defined - just as y in the example above.
