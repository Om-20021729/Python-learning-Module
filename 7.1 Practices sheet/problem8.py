# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("Enter a input name:  "))  # Taking an integer input from the user
for i in range(1, n+1):  # Looping from 1 to n (inclusive)
    print("*" * i, end="")  # Printing i stars for the current row
    print("")  # Moving to the next line after printing stars for the current row
