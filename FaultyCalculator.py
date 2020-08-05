#   This is a faulty calculator

#   45*3 = 555 , 56 + 9 = 77, 56/6 = 4

print("Chose the operation which you want to perform")
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
operator = int(input("\n"))
print("\n Enter first number")
num1 = int(input("\n"))
print("\n Enter second number")
num2 = int(input("\n"))

if operator == 1 and num1 == 56 and num2 == 9:
    print("sum is ", 77)
elif operator == 3 and num1 == 45 and num2 == 3:
    print("Multiplication is ", 555)
elif operator == 4 and num1 == 56 and num2 == 6:
    print("Division is ", 4)
elif operator == 1:
    print("Sum is ", (num1 + num2))
elif operator == 2:
    print("Subtraction is ", num1 - num2)
elif operator == 3:
    print("Multiplication is ", num1 * num2)
elif operator == 4:
    print("Division is ", num1 / num2)
