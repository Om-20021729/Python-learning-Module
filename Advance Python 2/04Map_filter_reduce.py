from functools import reduce

# Map example
# Map applies a function to all the items 
# in an input_list.

# Syntax.

# map(function, input_list)
# the function can be lambda function

l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqlist = map(square, l)  # Pass 'l' instead of '1'
print(list(sqlist))  # Convert the map object to a list for display

"""Filter"""


#** Filter creates a list of items 
# for which the function returns true.

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))


# Reduce applies a rolling 
# computation to sequential pair of elements

# example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))


