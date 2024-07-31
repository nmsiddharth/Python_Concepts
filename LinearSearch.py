
list = [5,8,4,6,9,2]
n = 9

pos = -1

def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos'] = i
            return True

    return False

if search(list,n):
    print("Found At ",pos)
else:
    print("Not found")

