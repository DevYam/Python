#   Using functions in python
a = 10
b = 20

c = sum((a, b))  # Sum function takes an iterable as an argument e.g tuple or list
print(c)


def function1(a, b):
    print("Hi, This is function 1", a + b)


function1(12, 13)


def function2(a, b):
    """This is function2's docstring"""
    average = (a + b) / 2
    print(average)
    return average


v = function2(4, 13)
print(v)
print(function2.__doc__)
