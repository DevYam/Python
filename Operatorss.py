#   Operators in Python
#     Arithmetic operators
#     comparision operators
#     bitwise operators
#     logical operators
#     membership operators
#     assignment operators

#   Arithmetic operator

#   Addition, Subtraction, multiplication and division operator as usual

#   Floor division operator (Double divide //)
print("Double division of 12 and 5 is ", 12 // 5)  # IT will ignore the numbers after decimal

#   Exponential operator ( Double multiplication operator **)
print(" 5 raise to the power 3 is ", 5 ** 3)

#     logical operators
a = True
b = False
print(a and a)
print(a and b)
print(b and b)

# Identity operator
print(a is b)
print(a is not b)

#     membership operators
list1 = [2, 3, 33, 43, 56]
print(33 in list1)
print(333 in list1)
print(22 not in list1)

#     bitwise operators

# 1 = 01
# 2 = 10
# 3 = 11
print(1 & 2)
print(1 | 3)
