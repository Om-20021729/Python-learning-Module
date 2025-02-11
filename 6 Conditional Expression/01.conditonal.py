# conditional statements/ expressions

# Sometimes we want to play PUBG on our phone if the day is Sunday.
# Sometimes we order Ice Cream online if the day is sunny.
# Sometimes we go hiking if our parents allow.


# All these are decisions which depend on a condition being met.

# In python programming too, we must be able to execute instructions on a condition(s) being met.
# This is what conditionals are for!

# IF STATEMENT
# marks = 97
# if marks>=90:
#    print("you will get a mobile phone")

# IF-ELSE STATEMENT

# a=22
# if(a>9):
#  print("greater")
# else:
#  print("lesser")

#  IF ELSE AND ELIF IN PYTHON
#
#  If else and elif statements are a multiway decision taken by our program due to certain
# conditions in our code.

# Syntax:

# if (condition1): # if condition1 is True
# print ("yes")
# elif(condition2): # if condition2 is True
# print("no")
# else: # otherwise
# print("maybe")

# Nested if statements

"""marks = 78
if marks>=80:
   print("you will get a new phone")
if marks>=95:
   print("you can go to a trip")
else:
   print("no phone for a month")"""




# some examples of conditional expressions
# if else statements


age = int(input("Enter your age:  "))
"""if(a>=18):
   print("Your are above the age of consent")
   print("Good for you")
else:
   print("You are Below the age of Consent")

print("End of Program")"""

# If elif else ladder

"""if(a>=18):
   print("Your are above the age of consent")
   print("Good for you")

elif(a<0):
   print("You are entering an invalid negative age")

elif(a==0):
   print("You are entering 0 which is not a valid age")

else:
   print("You are Below the age of Consent")


print("End of Program")"""

# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

# if age>=18:
#    print("Yes ")
# else:
#    print("No ")


# RELATIONAL OPERATORS

# Relational Operators are used to evaluate conditions inside the if statements. Some
# examples of relational operators are:
# ==: equals.
# > =: greater than/ equal to.
# < =: lesser than/ equal to.

# LOGICAL OPERATORS

# In python logical operators operate on conditional statements. For Example:
# • and – true if both operands are true else false.
# • or – true if at least one operand is true or else false.
# • not – inverts true to false & false to true.



# IMPORTANT NOTES:

# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions 
#    inside elifs fail.