
pos = -1

def search(list, n):
    l =0
    u = len(list)-1

    while l<=u:
        mid = (l+u)//2  # // it use for Interger division

        if list[mid]==n:
            globals()["pos"] = mid
            return True

        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

list = [1,2,3,4,5,6,7,8,9,0]
n = 44

if search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")