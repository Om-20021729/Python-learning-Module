# Raising Exceptions

# We can raise custom exceptions
# using the ‘raise’ keyword in python.
a = int(input("enter a num: "))
b = int(input("enter second num: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meantto divide by zero")
else:
    print(f"the division a/b is {a/b}")