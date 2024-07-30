class Square:
    def __init__(self,num):
        self.num = num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.num:
            raise StopIteration
        result = self.current ** 2
        self.current+=1
        return result

sq = Square(5)

for i in sq:
    print(i)