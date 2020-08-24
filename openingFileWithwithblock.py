with open("asked.txt") as f:
    print(f.readline())

"""
While reading file using with block we do not have 
to take care of closing file, this is automatically
handled by with block.
"""
