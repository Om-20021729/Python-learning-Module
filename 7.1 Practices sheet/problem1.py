#  Write a program to print multiplication table of a given number using for loop.
n = int(input("enter a number:  "))
# for i in range(1,11):
#     print(i*n)

# alternate method
"""for i in range(1,11):
    print(f"{n} x {i} = {n * i}")"""



## In while loop 


i = 1

while i < 11:  # Loop until i is 10
    print(f"{n} x {i} = {n * i}")
    i += 1
