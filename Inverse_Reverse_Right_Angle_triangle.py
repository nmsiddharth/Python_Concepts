rows = 4

for i in range(1,5):
    for k in range(i):
        print("  ",end="")
    for j in range(rows,i-1,-1):
        print("# ",end="")
    print()