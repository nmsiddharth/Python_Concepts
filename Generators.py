def Square(num):
    current = 1

    while current<=num:
        yield current ** 2
        current +=1

for i in Square(5):
    print(i)
