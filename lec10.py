#  Dictionary is a data structure and is used to store key value pairs as it is done in real life dictionaries

d1 = {}
print(type(d1))  # class dict ==> Dictionary (key value pair)

d2 = {"Divyam": "test", "test2": "testing", "tech": "guru", "dict": {"a": "dicta", "b": "dictb"}}
print(d2)
print(d2["Divyam"])  # Keys of dictionary are case sensitive
# print(d2["0"]) ==> Error

print(d2["dict"]["b"])  # queering nested dictionary

# The values in the key value pair of dictionary can be a list, tuple,
# dictionary etc but the key should be of immutable type . e.g String or numbers

# Adding new items to dictionary
d2["added"] = "newlyAdded"
print(d2)

#  dictionary keys can be numbers as well
d2[420] = "I am 420"
print(d2)

# deleting key 420 from dictionary

del d2[420]
print(d2)  # Element with key 420 got deleted

d3 = d2  # here it will behave as pass by reference
del d3["added"]
print(d2)  # key with element added got deleted from d2 as well

# To avoid this we will use copy function

d4 = d2.copy()
del d4["Divyam"]
print(d2)  # not deleted from original dictionary
print(d4)  # Deleted from copy

print(d2.get("Divyam"))

d2.update({"opem": "sankore"})
print(d2)

print(d2.keys())
print(d2.values())

print(d2.items())  # prints full key value pairs
