# Typecasting in python
numStr = "23"
numStr1 = "32"
print(numStr+numStr1) #output 2332
print(int(numStr)+int(numStr1)) #output 55

"""
Typecasting functions in python
int()
str()
float()
"""

# Printing hello world 100 times
print(100 * "Hello world")

# Printing hello world 100 times with new line
print(100 * "Hello world\n")

# Doing this thing with number will not work directly we will have to first cast the output to string

var1 = "80"
var2 = "43"
print(100*(str(int(var1)+int(var2))+"\n"))

# Input function

print("Enter a number")
inpNum = input()        # Input will go to the variable as a string
print("You Entered "+inpNum)  # This also works
print("You Entered ", inpNum)  # NOTE the syntax

print("Enter first number")
inpNum1 = input()
print("Enter Second number")
inpNum12 = input()
print("String addition is "+inpNum1+inpNum12)
""" Here the output will come as a concatenated number not addition we will have to 
typecast it to get the sum """
print("sum is ",int(inpNum1)+int(inpNum12))

