#   Take user input to print * triangle pattern
#   also take a boolean from user to print upright or inverted * triangle

rows = int(input("Enter the number of rows wanted in the triangle * pattern\n"))
orientation = bool(input("Enter 0 for inverted and 1 for upright triangle\n"))

if orientation == 1:
    for i in range(rows):
        print(" ")
        for j in range(i):
            print("* ", end="")

# if orientation == 0:
#     for i in range(rows):
#         print("* ")
#         for j in range(i):
#             print(" ", end="")
