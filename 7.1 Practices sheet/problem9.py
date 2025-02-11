# 9. Write a program to print the following star pattern.

# * * *
# *   *                 for n = 3
# * * *

"""n = int(input("Enter a number:   "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")"""

# alternate method
 


"""
n = int(input("Enter the size of the square: "))  # Input for the size of the square

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  # Print the top and bottom rows filled with '*'
    else:
        print("*" + " " * (n - 2) + "*")  # Print middle rows with spaces in between
        
        
        """