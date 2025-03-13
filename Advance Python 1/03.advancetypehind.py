# Python's typing module provides more advanced type hints, such as List, Tuple, Dict,
# and Union.
# You can import List, Tuple and Dict types from the typing module like this:

from typing import List, Tuple, Dict, Union

# list of integers
numbers : List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integers
person: Tuple[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123"
identifier = 12345 # ALSO valid

# These annotations help in making the code self-documenting and allow developers to
# understand the data structures used at a glance.
