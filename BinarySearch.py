list = [5,8,4,6,9,2]
n = 5
list.sort()
print(list)
def search(list,n):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2  # Floor division for integers {just like " % " in Java }
        if list[mid] == n:
            return mid
            break
        elif list[mid] < n:
            low = mid + 1
        elif list[mid] > n:
            high = mid - 1
    else:
        return -1

pos = search(list,n)

if pos!=-1:
    print("Found At ", pos)
else:
    print("Not found")