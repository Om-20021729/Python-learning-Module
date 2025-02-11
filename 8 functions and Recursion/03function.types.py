# TYPES OF FUNCTIONS IN PYTHON

# There are two types of functions in python:

# • Built in functions (Already present in python)
# • User defined functions (Defined by the user)

# Examples of built in functions includes len(), print(), range() etc.

# The func1() function we defined is an example of user defined function.

# def func1():
#     print('hello')

# func1()

# function with arguments
'''
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

goodDay("Rudra", "Thanks you")

'''
# FUNCTIONS WITH ARGUMENTS

# A function can accept some value it can work with.
# We can put these values in the parentheses.

# A function can also return value 
'''

def greet(name):
    gr = "hello " + name
    return gr

a = greet ("harry")
print(a)

'''
# a will now contain "hello harry"

'''
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

a = goodDay("Harry", "Thanks you")
print(a) '''


# DEFAULT PARAMETER VALUE


# We can have a value as default as default 
# argument in a function.
'''
def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks")
goodDay("Rohan")

If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.


Example:

def greet(name = "stranger"):
# function body
greet() # name will be "stranger" in function body (default)
greet("harry") # name will be "harry" in function body (passed)




'''