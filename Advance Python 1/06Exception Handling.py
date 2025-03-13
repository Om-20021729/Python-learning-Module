# EXCEPTION HANDLING IN PYTHON
# There are many built-in exceptions 
# which are raised in python when something goes
# wrong.

#  Exception in python can be handled 
# using a try statement. The code that handles the
# exception is written in the except clause.


# Exception handling means catching and 
# handling errors so that your program doesn’t 
# crash — you can show a friendly 
# message or take other action instead.


# try:
# # Code which might throw exception
# except Exception as e:
# print(e)


try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print(v)
except Exception as e:
    print(e)

print("Thank You")