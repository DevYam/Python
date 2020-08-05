var1 = 13
var2 = 31

var3 = int(input("Enter a number to check\n"))

# if var3 > var2:
#     print("greater")
# if var3 == var2:
#     print("Equal")
# else:
#     print("lesser")

#   If we use only if statements to check the conditions then it will go inside every if and it will be time taking
#   to avoid this we use if else statements, it is also called if else ladder in python else if is abbreviated as elif

if var3 > var2:
    print("greater")
elif var3 == var2:
    print("Equal")
else:
    print("lesser")

list1 = [2, 5, 7, 11]

if 5 in list1:
    print("5 is in list")

    # in keyword id used to check if an element is present in a list
print(5 in list1)
print(51 in list1)

# not in list

print(5 not in list1)
print(51 not in list1)
