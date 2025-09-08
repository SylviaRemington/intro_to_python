# This is a comment! Python will ignore it.

"""
THESE ARE CALLED DOC STRINGS IN PYTHON
this is a
multiline comment
"""

'''
this is also a multiline comment
you can use either set of quotes
'''

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

print(type("hello"))
# prints: <class 'str'>

print(type(25))

print(type(3.141592654))

print(type(True))

print(type(None))
# prints: `<class 'NoneType'>`

num_tacos = 25
# this won't work msg = "There are " + num_tacos + " tacos."
# TypeError: can only concatenate str (not "int") to str

msg = "There are " + str(num_tacos) + " tacos." #this will work because creating a string
print(msg)

# str(item)        # Converts `item` to a string
# int(item, base)  # Converts `item` to an integer with the provided `base`
# float(item)      # Converts `item` to a floating-point number
# hex(int)         # Converts `int` to a hexadecimal string
# oct(int)         # Converts `int` to an octal string
# tuple(item)      # Converts `item` to a tuple
# list(item)       # Converts `item` to a list
# dict(item)       # Converts `item` to a dictionary


