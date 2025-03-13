# THE GLOBAL KEYWORD

# ‘global’ keyword is used to modify the variable 
# outside of the current scope.


# Problem without global:

# x = 5

# def change():
#     x = 10  # This creates a new local variable, doesn't change the global one

# change()
# print(x)  # Output: 5  (not 10)

# Solution using global:

x = 5

def change():
    global x  # Tell Python to use the global x
    x = 10

change()
print(x)  # Output: 10