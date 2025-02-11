# 6. Write a python function which 
# converts inches to cms.

# "1inch = 2.54cm"
#  "ninch = n * 2.54"
 
def inch_to_cms(inch):

    return inch * 2.54

n = int(input("Enter value in inches:  "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")
