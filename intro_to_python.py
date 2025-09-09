# This is a comment! Python will ignore it.

# """
# THESE ARE CALLED DOC STRINGS IN PYTHON
# this is a
# multiline comment
# """

# '''
# this is also a multiline comment
# you can use either set of quotes
# '''

# this is a
# multiline comment


# print("Hello, world!") # prints: Hello, world!

num = 15

movie = 'Diehard'
# movie
# returns: NameError: name 'movie' is not defined
# this is illegal syntax that cannot be used

# in Python, we use snake_case
my_number = 10
# print(my_number)

my_number = -5
# print(my_number)

MY_FAVORITE_NUMBER = 5
# This communicateds that variable is not meant to be reassigned... however
# it can be reassigned. This is called SCREAMING_SNAKE_CASE.
# Class of string
print(type("wuzzup"))

# '''
# - Python is a true object-oriented programming language.
# - Every piece of data in Python is an object that's an instance of a class.
# - A class is a blueprint for creating objects. This means that a string object will have 
# different attributes and methods than an integer object because the string was created from 
# a different blueprint than the integer.
# '''

# Class of string - class is a blueprint for printing out these objects
print(type("hello"))
# prints: <class 'str'>


# Below is class of integer - whole numbers
print(type(25))


# floating numbers - numbers with decimal in them
print(type(3.141592654))


# booleans in conditional expressions - except they are written with capitals - e.g. True or False
print(type(True))


# Similar to JS's null and undefined (python kind of combines the two)
print(type(None))
# prints: `<class 'NoneType'>`


num_tacos = 25
# this won't work right here --> msg = "There are " + num_tacos + " tacos."
# TypeError: can only concatenate str (not "int") to str
# no type coercion in python


msg = "There are " + str(num_tacos) + " tacos." 
#this will work because creating a string
# Have to change the number to a string and then add three strings together.

# python is printing out the message for the above string combination
print(msg)


# str(item)        # Converts `item` to a string
# int(item, base)  # Converts `item` to an integer with the provided `base`
# float(item)      # Converts `item` to a floating-point number
# hex(int)         # Converts `int` to a hexadecimal string
# oct(int)         # Converts `int` to an octal string
# tuple(item)      # Converts `item` to a tuple
# list(item)       # Converts `item` to a list
# dict(item)       # Converts `item` to a dictionary

# --------------------------------------------------------------------------

# Performing Mathematical Operations in Python
# Python has the normal math operators that you are used to from JavaScript:

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulo (remainder) (%)
# Exponentiation (**)

new_num = 10 ** 2
print(new_num)

# Integer Division
result = 4 / 2
print(result)
# In the answer, it gave us a float

# You can force it to give an integer if you add two //
result = 4 // 2
print(result)
# It's flooring doing this division.


result = 5 // 2
print(result)
# It's flooring doing this division.
# This means that it will still give an integer even if the actual answer is 2.5
# It rounds it down.

# --------------------------------------------------------------------------

# Shortcut Assignment Operators
# Notice no linting errors which shows it is valid linting code

# this line of code:
num = num + 1
# can be written with this shortcut operator:
num += 1

# it also works for any of the other math operations:
num = num / 5
# can be rewritten like this:
num /= 5

# and this line:
num = num * 3
# can be written as this:
num *= 3
# and so on with the other operators

# --------------------------------------------------------------------------

# Can't use num++
# A couple of our favorite operators in JavaScript, increment (++) and decrement (–), 
# do not exist in Python. Use += 1 and -= 1 instead.

# --------------------------------------------------------------------------

# Working with Strings
# Write multiline strings, perform string interpolation, and use string methods to work with 
# string types in Python
my_string = "A double-quoted string"
your_string = 'A single quoted string'

multiline_string = '''This is my string that
                      goes on multiple lines
                      for whatever reason'''

# Above assigning it to a variable so that we can work with it later - so there is a relationship
# with comments and strings


# Concatenating strings
little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints: superbad


# String interpolation using f-Strings
state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
print(message)
# prints: Hawaii was the last state to join the U.S. in 1959.


# Useful String Methods

print("ace of spades".split(" "))
# prints: ['ace', 'of', 'spades']

# however, this won't work:
# print("abcd".split(""))
# ValueError: empty separator
# It's calling a split method directly on a string.

# instead, use the list() function like this:
print(list("abcd"))
# prints: ['a', 'b', 'c', 'd']

# get the index of a substring:
print("abcd".index("c"))    
# prints: 2

# this method raises an error if the substring is not found:
# print("abcd".index("e"))
# ValueError: substring not found

# .find() is similar to .index() but returns -1 if the substring is not found
# this behavior may be preferable to raising an error:
print("abcd".find("e"))
# prints: -1

# uppercase - changing everything to uppercase in python
print("boo".upper())
# prints: 'BOO'

# lowercase - changing everything to lowercase in python
print("WHY???".lower())
# prints: 'why???'

print("Then I went to the store I like".replace("I", "you"))
# prints: 'Then you went to the store you like'


# in operator - checking if string contains a substring
print("eggs" in "green eggs and ham")
# prints: True


# len() function - is the length of the string
print(len("Tacos"))
# prints: 5
