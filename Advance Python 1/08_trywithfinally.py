# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
# the exception.
try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("hey I am inside code")