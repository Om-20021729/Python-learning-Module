# Sets:
# Set is a collection of non-repetitive elements.
 
# s ={1, 5, 32, 54, 5, 5, 5}

# e = set() # dont use s = {} as it will create an empty dictionary.
# s.add(5546)
# print(s, type(s))

# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# Operations on sets
# add(element): Adds an element to the set. If the element already exists, it does nothing.


# s = {1, 2, 3}
# s.add(4)
# print(s)  # Output: {1, 2, 3, 4}

# discard(element): Removes the specified element from the set if it exists; otherwise, it does nothing.

# s = {1, 2, 3}
# s.discard(2)
# print(s)  # Output: {1, 3}
# s.discard(5)  # No error, even though 5 is not in the set

# difference(*others): Returns a new set containing elements present in the set but not in the specified sets.

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# diff = s1.difference(s2)
# print(diff)  # Output: {1}
#
#  difference_update(*others): Removes elements found in the specified sets from the original set.

#  s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s1.difference_update(s2)
# print(s1)  # Output: {1}
#
#  symmetric_difference(other): Returns a new set with elements in either the set or the other set, but not in both.

# s1 = {1, 2, 3}
# s2 = {3, 4}
# sym_diff = s1.symmetric_difference(s2)
# print(sym_diff)  # Output: {1, 2, 4}

# symmetric_difference_update(other): Updates the set to be the symmetric difference of itself and another.


# s1 = {1, 2, 3}
# s2 = {3, 4}
# s1.symmetric_difference_update(s2)
# print(s1)  # Output: {1, 2, 4}

# issubset(other): Returns True if all elements of the set are in another set.


# s1 = {1, 2}
# s2 = {1, 2, 3}
# print(s1.issubset(s2))  # Output: True

# issuperset(other): Returns True if all elements of another set are in the set.

# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1.issuperset(s2))  # Output: True

# isdisjoint(other): Returns True if the set has no elements in common with another set.


# s1 = {1, 2}
# s2 = {3, 4}
# print(s1.isdisjoint(s2))  # Output: True