# tuple method
# a = (1, 7, 2)
# • a.count (1): a count (1) will return number of times 1 occurs in a.
# • a.index (1) will return the index of first occurrence of 1 in a.

# Tuples in Python are immutable sequences, meaning their elements cannot be changed after creation.

# ### **1. `count()`**
# - **Description**: Returns the number of times a specified value occurs in a tuple.
# - **Syntax**: `tuple.count(value)`
# - **Example**:
#   my_tuple = (1, 2, 3, 2, 2, 4)
#   print(my_tuple.count(2))  # Output: 3

# ### **2. `index()`**
# - **Description**: Returns the first index of the specified value in the tuple. Raises a `ValueError` if the value is not found.
# - **Syntax**: `tuple.index(value)`
# - **Example**:
#   ```python
#   my_tuple = (1, 2, 3, 2, 4)
#   print(my_tuple.index(2))  # Output: 1
 
# ### **3. Tuple Concatenation**
# - **Description**: Combines two or more tuples.
# - **Syntax**: `tuple1 + tuple2`
# - **Example**:
#   ```python
#   tuple1 = (1, 2, 3)
#   tuple2 = (4, 5, 6)
#   result = tuple1 + tuple2
#   print(result)  # Output: (1, 2, 3, 4, 5, 6)
 
# ### **4. Tuple Repetition**
# - **Description**: Repeats a tuple a specified number of times.
# - **Syntax**: `tuple * n`
# - **Example**:
#   ```python
#   my_tuple = (1, 2, 3)
#   result = my_tuple * 3
#   print(result)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ### **5. Membership Testing**
# - **Description**: Checks if an element exists in a tuple.
# - **Syntax**: `value in tuple`
# - **Example**:
#   ```python
#   my_tuple = (1, 2, 3)
#   print(2 in my_tuple)   # Output: True
#   print(5 in my_tuple)   # Output: False
 
# ### **6. Length of Tuple**
# - **Description**: Returns the number of elements in a tuple.
# - **Syntax**: `len(tuple)`
# - **Example**:
#   ```python
#   my_tuple = (1, 2, 3, 4)
#   print(len(my_tuple))  # Output: 4
  
# ### **7. Slicing**
# - **Description**: Extracts a subset of the tuple.
# - **Syntax**: `tuple[start:end:step]`
# - **Example**:
#   ```python
#   my_tuple = (0, 1, 2, 3, 4, 5)
#   print(my_tuple[1:4])  # Output: (1, 2, 3)
#   print(my_tuple[::-1]) # Output: (5, 4, 3, 2, 1, 0)
 
# ### **8. Tuple Unpacking**
# - **Description**: Assigns tuple elements to variables.
# - **Syntax**: `var1, var2, ... = tuple`
# - **Example**:
#   ```python
#   my_tuple = (1, 2, 3)
#   a, b, c = my_tuple
#   print(a, b, c)  # Output: 1 2 3
 
# ### **9. Nested Tuples**
# - **Description**: Tuples can contain other tuples.
# - **Example**:
#   ```python
#   nested_tuple = (1, (2, 3), (4, 5, 6))
#   print(nested_tuple[1])  # Output: (2, 3)
#   print(nested_tuple[2][1])  # Output: 5

# ### **10. Conversion to Tuple**
# - **Description**: Converts an iterable (like a list or string) to a tuple.
# - **Syntax**: `tuple(iterable)`

#   my_list = [1, 2, 3]
#   my_tuple = tuple(my_list)
#   print(my_tuple)  # Output: (1, 2, 3)
