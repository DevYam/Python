age = int(input("Enter your age\n"))
if age < 18:
    print("You are too young to drive")
elif age == 18:
    print("Contact us we will think about you")
elif 18 < age < 100:
    print("You can drive")
elif 99 < age < 200:
    print(" you are too old to drive")
else:
    print(" Enter a valid age")
