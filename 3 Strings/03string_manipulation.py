# Here are some of the most commonly used string functions in Python:

# ### 1. **`len()`**
#    - **Purpose**: Returns the length of the string.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(len(s))  # Output: 5
#      ```

# ### 2. **`lower()`**
#    - **Purpose**: Converts all characters in the string to lowercase.
#    - **Example**: 
#      ```python
#      s = "HELLO"
#      print(s.lower())  # Output: hello
#      ```

# ### 3. **`upper()`**
#    - **Purpose**: Converts all characters in the string to uppercase.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.upper())  # Output: HELLO
#      ```

# ### 4. **`strip()`**
#    - **Purpose**: Removes leading and trailing whitespace (or specified characters).
#    - **Example**: 
#      ```python
#      s = "  hello  "
#      print(s.strip())  # Output: hello
#      ```

# ### 5. **`replace()`**
#    - **Purpose**: Replaces occurrences of a substring with another substring.
#    - **Example**: 
#      ```python
#      s = "hello world"
#      print(s.replace("world", "Python"))  # Output: hello Python
#      ```

# ### 6. **`split()`**
#    - **Purpose**: Splits the string into a list based on a delimiter.
#    - **Example**: 
#      ```python
#      s = "a,b,c"
#      print(s.split(","))  # Output: ['a', 'b', 'c']
#      ```

# ### 7. **`join()`**
#    - **Purpose**: Joins elements of a list into a single string with a specified delimiter.
#    - **Example**: 
#      ```python
#      lst = ['a', 'b', 'c']
#      print(",".join(lst))  # Output: a,b,c
#      ```

# ### 8. **`find()`**
#    - **Purpose**: Returns the index of the first occurrence of a substring; returns `-1` if not found.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.find("e"))  # Output: 1
#      ```

# ### 9. **`count()`**
#    - **Purpose**: Returns the number of occurrences of a substring.
#    - **Example**: 
#      ```python
#      s = "hello hello"
#      print(s.count("hello"))  # Output: 2
#      ```

# ### 10. **`startswith()`**
#    - **Purpose**: Checks if the string starts with a specified substring.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.startswith("he"))  # Output: True
#      ```

# ### 11. **`endswith()`**
#    - **Purpose**: Checks if the string ends with a specified substring.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.endswith("lo"))  # Output: True
#      ```

# ### 12. **`capitalize()`**
#    - **Purpose**: Capitalizes the first character of the string.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.capitalize())  # Output: Hello
#      ```

# ### 13. **`title()`**
#    - **Purpose**: Converts the first character of each word to uppercase.
#    - **Example**: 
#      ```python
#      s = "hello world"
#      print(s.title())  # Output: Hello World
#      ```

# ### 14. **`isalpha()`**
#    - **Purpose**: Checks if the string contains only alphabetic characters.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.isalpha())  # Output: True
#      ```

# ### 15. **`isdigit()`**
#    - **Purpose**: Checks if the string contains only digits.
#    - **Example**: 
#      ```python
#      s = "12345"
#      print(s.isdigit())  # Output: True
#      ```

# ### 16. **`isalnum()`**
#    - **Purpose**: Checks if the string contains only alphanumeric characters.
#    - **Example**: 
#      ```python
#      s = "hello123"
#      print(s.isalnum())  # Output: True
#      ```

# ### 17. **`islower()`**
#    - **Purpose**: Checks if all characters in the string are lowercase.
#    - **Example**: 
#      ```python
#      s = "hello"
#      print(s.islower())  # Output: True
#      ```

# ### 18. **`isupper()`**
#    - **Purpose**: Checks if all characters in the string are uppercase.
#    - **Example**: 
#      ```python
#      s = "HELLO"
#      print(s.isupper())  # Output: True
#      ```

# ### 19. **`swapcase()`**
#    - **Purpose**: Swaps the case of all characters in the string.
#    - **Example**: 
#      ```python
#      s = "Hello World"
#      print(s.swapcase())  # Output: hELLO wORLD
#      ```

# ### 20. **`zfill()`**
#    - **Purpose**: Pads the string with zeros on the left to make it a specific length.
#    - **Example**: 
#      ```python
#      s = "42"
#      print(s.zfill(5))  # Output: 00042