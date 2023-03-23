# Dictionary - {}
# Dictionary will be created with key and value pairs
# Dictionary does not allow duplicate keys
# Dictionary is mutable

d1 = {'name': 'Indrajit', 'age': 20}
d2 = {"fruits" : "apple", "language" : "english", "year": 1993, "year": 2001} # duplicate key will be overwritten
print(d2)
type(d2)
print(len(d2))

#You can refer to the value of a key using the key name
print(d2["fruits"])
# Printing keys
print(d2.keys())
# Using get() method
print(d2.get("fruits"))

d2 ["color"] = "white" # This will create a new key and value pair
print(d2)

#values() method
print(d2.values())

#items() method
print(d2.items())

#update() method
d2.update({"color" : "red"})

#items() method
print(d2.items())

#pop() method
d2.pop("color")

#pop item
print(d2.popitem())

# delete key
del d2["fruits"]

# clear() method
d2.clear()

for x in d2.values():
    print(x)

for x in d2.keys():
    print(x)

for x in d2.items():
    print(x)

# Copy a dictionary
d3 = d2.copy() #copy() method
print(d3)



d3 = {
    'name': 'Indrajit', 
    'age': 20, 
    'fruits': 'apple', 
    'language': 'english', 
    'year': 1993, 
    "colours" : ["red", "green", "blue"]
    }

d4 = {
    'name': "Ram",
    "year": 1997
    }

d5 = {
    'name': "Sam",
    "year": 1997
    }

final = {
    "d3" : d3,
    "d4" : d4,
    "d5" : d5
    }

# print(final)


# Dictionary methods

# clear() , copy() , fromkeys() , get() , items() , keys() , pop() , popitem() , setdefault() , update() , values()

for key, value in d3.items():
    print(key, value)