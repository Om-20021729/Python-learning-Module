# 7. Write a python function to remove a given word from 
# a list ad strip it at the same time.


# so we need to solve the part one by one 
def rem(l, word):
    n = []
    for item in l:        # ab har word se an hatana ha toh .strip function use karna ha 
        if not(item == word):
            n.append(item.strip(word))
    return n 

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))