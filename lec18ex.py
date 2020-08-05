#  This program will continue taking input unless the user enters a value grater than 10

while True:
    inp = input("Enter a number\n")
    if int(inp) > 100:
        print("Congratulations you entered a value greater than 100")
        break

