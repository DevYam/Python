#   Using for loop print only numbers which are greater than 6
list1 = ["divyam", "Kumar", "Singh", "1", "4", "age", "7", "23"]

for item in list1:
    if item.isdigit():
        if int(item) > 6:
            print(item)
