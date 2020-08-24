# f = open("divyam2.txt", "a")  # Here f is not pointer like c++ this is called file handle, opening file in write mode
# # #   Giving a new file name here will create a new file
# # a = f.write("\nThis is written using python")
# # print(a)    # a will print the number of characters written to the file
# # f.close()


#   Handle read and write both
f = open("divyam.txt", "r+")
print(f.read())
f.write("Thank you")
