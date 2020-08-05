#   Break and continue in python

# i = 0
# while i < 45:
#     print(i+1, end=" ")
#     i = i+1

j = 0
while True:

    if j < 5:
        j = j + 1
        continue
    print(j)
    j = j + 1
    if j == 46:
        break
