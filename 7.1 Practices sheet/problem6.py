# problem of factorial
n = int(input("Enter a number is :  "))
product = 1 

for i in range(1,n+1):
    product = product * i

print(f"the factorial of {n} is {product}")