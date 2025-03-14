# Functions and Recursion



# Functions: A function is
#  a group of statements performing 
#  a specific task.



# When a program gets bigger in size and 
# its complexity grows, it gets difficult for a
# program to keep track on which piece of code 
# is doing what!


# A function can be reused by the programmer
#  in a given program any number of


# examples
# function defination
def avg():
    a = int(input("Enter your number a here:  "))
    b = int(input("Enter your number b here:  "))
    c = int(input("Enter your number c here:  "))

    average = (a + b + c)/3
    print(average)

avg()
avg()     #function call
avg()


'''
EXAMPLE AND SYNTAX OF A FUNCTION

The syntax of a function looks as follows:
def func1():
    print('hello')


This function can be called any number of times, anywhere in the program.
FUNCTION CALL

Whenever we want to call a function, we put the name of the function followed by
parentheses as follows:


func1() # This is called function call.


FUNCTION DEFINITION
The part containing the exact set of instructions which are executed during the function
call.

'''