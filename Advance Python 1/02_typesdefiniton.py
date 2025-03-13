# TYPES DEFINITIONS IN PYTHON


#Type hints are added using the colon (:) syntax
#  for variables 
# and the -> syntax for
# function return types.


# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice")) # Output: Hello, Alice!

