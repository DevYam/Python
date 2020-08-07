f = open("divyam.txt", "rt")  # open function will return a file pointer which is stored in f

# mode can be rb == read in binary mode, rt == read in text mode
# content = f.read(3)     # Will read only 3 characters
# content = content + "20"
# content += "test"


# content = f.read(3)     # Will read next 3 characters
# print(content)

# content = f.read()
# print(content)

# for abc in content:
#     print(abc)      # Will print character by character

#   For printing line by line we can iterate over the pointer f

# for ab in f:
#     print(ab)   # This prints a new line character at the end of each line because that is present in text file
#

# for ab in f:
#     print(ab, end=" ")  # This prints line by line

# print(f.readline(), end=" ")    # This space in end=" " makes the second line move a little further
# print(f.readline())
# print(f.readline())

content = f.readline()
content += f.readline()
print(content)
# print(f.readlines())
f.close()
