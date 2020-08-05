# sets in python

s = set()
print(type(s))  # output => <class 'set'>

listVar = [1, 2, 2, 3, 4]
#  creating set from list in python
# setFromList = set([1, 2, 3, 4])
setFromList = set(listVar)  # duplicate value is eliminated it will not throw an error

print(setFromList)  # output => {1, 2, 3, 4}
print(type(setFromList))  # output => <class 'set'>

#    Adding elements to set s

s.add(1)
s.add(1)  # duplicate value not added to set
#    set retains unique values
s.add(2)  # the new value 2 got added
print(s)

#   There is built in union and intersection functions for sets in python
unionSet = s.union({1, 2, 3})
# print(s, unionSet)

print(unionSet)

intersectionSet = s.intersection({1})
print(intersectionSet)

#   length of a set
print(len(intersectionSet))
print(len(unionSet))

#   minimum and maximum elements of a set
print(min(s))
print(max(s))

newSet = {11, 21, 31, 51}
print(max(newSet))

#   Checking if two sets are disjoint or not

print(s.isdisjoint(newSet))

newSet.remove(11)
print(newSet)
