#   for loop in python
list1 = ["Divyam", "Kumar", "Singh"]
for item in list1:
    print(item)
#   Iterating through list of lists (Unpacking list of lists)
list2 = [["divyam", 23], ["kumar", 36], ["singh", 33]]
for item, weight in list2:
    print(item, weight)

dict1 = dict(list2)
print(dict1)

for item in dict1:
    print(item)

for item, weight in dict1.items():
    print(item, weight)
