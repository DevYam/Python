# Lecture 8
# String Slicing

myStr = "Divyam is a good boy"
print(myStr)
print(myStr[4])  # -> a
print(myStr[4:8])  # String slicing i.e, printing a part of a string  -> am i

# Length of a string len() function
print(len(myStr))
print(myStr[0:19])  # Printing full string

# Here the output is ->  "Divyam is a good bo" because the 19th index is excluding
print(myStr[0:20])  # Printing full string

# Skip alternate letter
print(myStr[0:6:2])  # -> Dva (Skipped one letter)
print(myStr[0:])  # Prints whole string - > took length as the last index
print(myStr[:6])  # Prints Divyam, took 0 as the starting index
print(myStr[4::2])  # Started from 4th index and and print whole file skipping every alternate character -> a sago o

# Slicing from behind
print(myStr[-2:-7])  # not working idk :(
print(myStr[::-2])  # Reversed the string and skipped one word

print(myStr[::-1])  # Reversed the string using slicing :) It was a pain in JAVA

# Checking alfa numeric string in python

print(myStr.isalnum())  # -> false
myNewStr = "3134jhleflsh23h4lhlhslhf"
print(myNewStr.isalnum())  # :) -> True
print(myNewStr.isalpha())  # -> false because contains numbers
print(myStr.isalpha())  # -> false because contains spaces
print(myStr.endswith("boy"))  # -> True

print(myStr.count("o"))  # -> 3

myUncapitalizedStr = "divyam is not capitalized"
print(myUncapitalizedStr.capitalize())  # The first character is made capital

print(myUncapitalizedStr.find("is"))
print(myStr.lower())
print(myStr.upper())
print(myStr.replace("is", "are"))
