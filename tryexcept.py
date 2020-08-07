a = input("Enter number 1\n")
b = input("Enter number 2\n")

try:
    print("Sum is ", int(a)+int(b))
except Exception as e:
    print(e)

print("This line is being printed after try except")
