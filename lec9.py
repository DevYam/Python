# list data type in python - > sorting, accessing and slicing etc
myItemList = ["Item1", "Item2", "freeItem", "fullBasket"]  # This is a list of integers, lly we can have list of
# integers and mixed list

myIntList = [23, 32, 2, 1, 33, 56, 65, 4, 5, 6, 78]
print(myItemList)
print(myIntList)

# Sort method on list in python shorts the original list
# myIntList.sort()
print(myIntList)

# Accessing list item using index
print(myItemList[0])  # -> Item1

# reverse the list
# myItemList.reverse()
print(myItemList)

# sort and reverse
myIntList.sort()
myIntList.reverse()
print(myIntList)

# List slicing in python

print(myItemList[0:3])
print(myItemList[:3])  # same as above

print(myItemList[:])  # Will take initial and final values automatically and will print the whole list
# Slicing returns a new list and the original list remains unchanged whereas sort and reverse function changes the
# original list

# Extended slicing
# This contains three parameters where the first parameter will indicate the starting index and 2nd parameter will
# indicate length of the list and the third parameter will indicate the jump.

print("This will print the full int list")
print(myIntList[::])

print("This will print the list partially")
print(myIntList[::2])  # here we have jump of 2

# PS - Don't use -2,-3 etc while slicing as it does not always only use -1 so as to reverse the list

print(len(myIntList))
print(max(myIntList))
print(min(myIntList))

print(myIntList)

myIntList.append(27)
print(myIntList)  # 27 got added to the list

myIntList.insert(2, 54)  # Inserts in between given the index
print(myIntList)

myIntList.remove(33)
print(myIntList)

myIntList.pop()
print(myIntList)  # removes the last number, same as stack's pop

myIntList[2] = 99
print(myIntList)  # 2nd index value got changed

# list is enclosed by [] and tuple is enclosed by ()
# list's value can change (Mutable)  but tuple's values can't change ( Immutable)

tp = (10, 20, 30)
# tp[1] = 23 This is an error as tuples are immutable

tp1 = (1)  # not a tuple considered as parenthesis
print(tp1)

tp2 = (1,)  # this is a valid tuple
print(tp2)

a = 21
b = 55

# now swap the values of a and b

print(a, b)
a, b = b, a
print(a, b)  # Numbers are swapped now
