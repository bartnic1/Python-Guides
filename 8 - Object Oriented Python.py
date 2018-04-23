# Up until now, we have been using an "imperative" style of programming. Here we issue commands to the computer which it
# follows in a defined order.

# Object oriented programming combines data and processes (that act on that data) into objects, which is called
# encapsulation.

# These two paradigms are not necessarily exclusive; object oriented programming makes use of imperative
# programming within the methods that objects use to manipulate their data. Also, imperative programming makes extensive
# use of objects.

# As an analogy, the imperative approach is similar to a recipe of cooking a meal. You start with the ingredients and
# utensils needed (the data), and continue with the description of the steps that must be performed on that data to
# produce a finished meal.

# An object oriented approach relies on the objects, such as the eggs, milk, spoon, etc. knowing how to perform certain
# operations. Then the program can tell each object to perform the relevant operation. For example, the egg object
# would have a process in which it fries itself. Since this is a bit odd, the imperative approach to cooking a meal is
# likely more appropriate than an object oriented one.

# Everything in Python is an object. It can be used for object oriented programming, or for imperative programming.

# -------------------------------------------------------------------------------------------------------------------- #

# Even in the simple case of addition, Python uses methods:

a = 12
b = 4
print(a + b)
print(a.__add__(b))

# If you ctrl + click on +, it shows you the same method as for __add__.

# Object oriented programming uses classes and methods to provide objects that encapsulate both data, and functions that
# operate on that data.

# When a function is part of a class, it is called a method. However, writing a method is the same as writing a
# function.

# Classes are a template from which objects can be created. All objects created from the same class will share the same
# characteristics, though their specific values may vary (i.e. below, the price could vary).

# An instance is just another name for an object created from a class definition. Thus, if a kettle
# called Kenwood were created uses a class, we could say Kenwood is an instance of the kettle class, or Kenwood is an
# object of type kettle.

# Example:


class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

# Here, we created an instance of the kettle class, called kenwood. We can access the characteristics using the
# "kenwood.characteristic" syntax.

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# When a variable is bound to an instance of a class, it is referred to as a data attribute in Python. In Java, these
# are called fields, while in C++ they are called data members.
