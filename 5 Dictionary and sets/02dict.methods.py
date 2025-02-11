a = {
    "name":"Rudra",
    "from":"Bharat",
    "marks":"Top rank in Commando course 300"
}
# print(a.items())  #a.items(): Returns a list of (key,value)tuples.
# print(a.keys())   #Returns a list containing dictionary's keys.
# print(a.values()) #Updates the dictionary with supplied key-value pairs
# a.update({"name": "Omkar"})
# print(a)

# print(a.get("name")) #  Returns the value of the specified keys (and value is returned
# eg."Rudra" is returned here).

# case1 output return same but both are different things
# print(a.get("name"))
# print(a["name"])

# case2 output different when 
# print(a.get("name1")) # print none
# print(a["name2"])  # retuns an error


# reason above explained

# If the key "name" exists in the dictionary a,
# both a.get("name") and a["name"] will return the same value. 
# However, if the key doesn't exist, their behavior differs 
# as explained above.

# Key Takeaway:
# Use .get() when you're unsure if the key exists and want to avoid a potential KeyError.
# Use [] when you are certain the key exists or when you want the program to fail explicitly if the key is missing.




# important key methods

# . pop(key[, default])
# Description: Removes the key and returns its value. If the key does not exist, it returns the default value (or raises a KeyError if no default is provided).

# a = {"name": "Alice", "age": 25}
# print(a.pop("age"))  # Output: 25
# print(a)  # Output: {'name': 'Alice'}

# 7. popitem()
# Description: Removes and returns the last key-value pair as a tuple (in Python 3.7+ dictionaries maintain insertion order).
# a = {"name": "Alice", "age": 25}
# print(a.popitem())  # Output: ('age', 25)
# print(a)  # Output: {'name': 'Alice'}

# 8. clear()
# Description: Removes all items from the dictionary, leaving it empty.

# a = {"name": "Alice", "age": 25}
# a.clear()
# print(a)  # Output: {}

# 9. setdefault(key[, default])
# Description: Returns the value of the key if it exists. If not, it inserts the key with the specified default value and returns the default value.
#  a = {"name": "Alice"}
# print(a.setdefault("age", 25))  # Output: 25
# print(a)  # Output: {'name': 'Alice', 'age': 25}

# 10. copy()
# Description: Returns a shallow copy of the dictionary.
# a = {"name": "Alice", "age": 25}
# b = a.copy()
# print(b)  # Output: {'name': 'Alice', 'age': 25}