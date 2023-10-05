pos = -1

def search(list, n):
    i =0
    while i<len(list):
        if list[i]==n:
            globals()["pos"] = i
            return True
        i = i +1
    return False

list = [12,22,3,1,4,9]
n=4

if search(list,n):
    print("Found at", pos+1)
else:
    print("Not Found")

# Linear Search Using For Loop

def search2(list1 , m):
    j =0

    for j in range(len(list1)):
        if list1[j]==m:
            globals()["pos"] = j
            return True
    return False

list1 = [1,2,3,45,5,6,7]
m = 45

if search2(list1,m):
    print("Found at", pos + 1)
else:
    print("Not Found")