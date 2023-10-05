f = open("MyData","r")

# print(f.read())  # It will print whole file
# print(f.readline()) # It will only print first line
# print(f.readline()) # It will only print 2nd line

# f = open("MyData","w")   # It is write type file
# f.write("I want laptop")  # it will clear all things from file & write "I want laptop" there

f1 = open("abc","w") # there is no "abc" file first so it create that first

for data in f:
    f1.write(data)  # then now it will add all the info in the "f/MyData" file in "abc / f1" file

