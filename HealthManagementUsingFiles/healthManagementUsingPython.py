# This is a health management system where we can keep record in files and retrieve them when needed

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
date = now.strftime("%d/%m/%Y")
# print("Current Time =", current_time)
f = open("personRecord.txt", "r+")
content = f.read()
if len(content) <= 0:
    print("Health Management System")
    people = int(input("Enter the number of people : "))
    peopleName = []
    for num in range(people):
        name = input("Enter name of person " + str(num + 1) + " : ")
        peopleName.append(name)
    print(peopleName)
    for name in peopleName:
        f.write(name + "\n")
    f.close()
else:
    # numberOfPersons = 0
    # f = open("personRecord.txt", "r+")
    # content = f.read()
    # splitContent = content.split("\n")
    # for name in splitContent:
    #     numberOfPersons += 1
    print("Welcome to Health Management System\nPlease choose one of the following\n")
    choice = int(input("1. Update Records\n2. View Records\n"))

    if choice == 1:

        f = open("personRecord.txt", "r+")
        numberOfRegs = f.readlines()
        print("You have " + str(len(numberOfRegs)) + " registered clients")
        for name in numberOfRegs:
            print(name, end="")
        clientName = input("Enter the client name whose record you want to update\n")

        optionValues = []
        f = open(clientName, "a")
        updateOptions = ["weight", "height", "Hours of exercise done"]
        for options in updateOptions:
            opt = input("Enter "+options + " :")
            optionValues.append(opt)
        f.write("Date = "+date+"\n")
        f.write("Time = "+current_time+"\n")
        for value in optionValues:
            f.write(value+"\n")
        f.close()
    elif choice == 2:
        f = open("personRecord.txt", "r+")
        numberOfRegs = f.readlines()
        print("You have " + str(len(numberOfRegs)) + " registered clients")
        for name in numberOfRegs:
            print(name, end="")
            f.close()
        clientName = input("Enter the client name whose record you want to view\n")
        f = open(clientName)
        records = f.readlines()
        print("Weight is "+records[len(records)-3], end="")
        print("height is "+records[len(records)-2], end="")
        print("Hours of exercise done is "+records[len(records)-1], end="")
        f.close()
