# # Sequence of characters after backslash "\" → Escape Sequence characters
# # Escape Sequence characters comprise of more than one character but represent one
# # character when used within the strings.
# # for ex : \n , \t , \' , \\ etc.
# a = "Om is a masculine man\nbut respect feminity as well"
# print(a)

# Escape sequences in Python are special characters preceded by a backslash (`\`) that represent specific actions or characters that are otherwise hard to include directly in a string. Here are the most commonly used escape sequences:

#  1. **`\n`** - Newline
#    - Inserts a new line in the string.
#    - **Example**:
#      ```python
#      print("Hello\nWorld")
#      # Output:
#      # Hello
#      # World
#      ```

# ### 2. **`\t`** - Horizontal Tab
#    - Inserts a horizontal tab space.
#    - **Example**:
#      ```python
#      print("Hello\tWorld")
#      # Output:
#      # Hello    World
#      ```

# ### 3. **`\\`** - Backslash
#    - Inserts a literal backslash (`\`).
#    - **Example**:
#      ```python
#      print("This is a backslash: \\")
#      # Output:
#      # This is a backslash: \
#      ```

# ### 4. **`\'`** - Single Quote
#    - Allows the use of a single quote inside a single-quoted string.
#    - **Example**:
#      ```python
#      print('It\'s a sunny day')
#      # Output:
#      # It's a sunny day
#      ```

# ### 5. **`\"`** - Double Quote
#    - Allows the use of a double quote inside a double-quoted string.
#    - **Example**:
#      ```python
#      print("He said, \"Hello!\"")
#      # Output:
#      # He said, "Hello!"
#      ```

# ### 6. **`\r`** - Carriage Return
#    - Moves the cursor to the beginning of the line without advancing to the next line.
#    - **Example**:
#      ```python
#      print("Hello\rWorld")
#      # Output:
#      # World
#      ```

# ### 7. **`\b`** - Backspace
#    - Removes the character before the escape sequence.
#    - **Example**:
#      ```python
#      print("Helloo\b World")
#      # Output:
#      # Hello World
#      ```

# ### 8. **`\f`** - Form Feed
#    - Moves the cursor to the next page or section.
#    - **Example**:
#      ```python
#      print("Hello\fWorld")
#      # Output:
#      # Hello
#      #      World
#      ```

# ### 9. **`\uXXXX`** - Unicode Character
#    - Inserts a Unicode character using a 16-bit hexadecimal code.
#    - **Example**:
#      ```python
#      print("\u2764")
#      # Output:
#      # ❤
#      ```

# ### 10. **`\xXX`** - Hexadecimal Character
#    - Inserts a character using a two-digit hexadecimal code.
#    - **Example**:
#      ```python
#      print("\x48\x69")
#      # Output:
#      # Hi
#      ```

# These escape sequences are crucial for handling special characters or formatting strings effectively in Python.a