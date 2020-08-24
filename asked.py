f = open("asked.txt","r+")

# f.close()

givenData = f.read()
number = 0
for a in givenData:
    if a.isdigit():
        number += int(a)

print(number)
f.write("\n"+str(number))
f.close()
