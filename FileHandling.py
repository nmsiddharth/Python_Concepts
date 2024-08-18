f = open('MyData','r')
print(f.readlines())
f1 = open("abc",'w')

for data in f:
    f1.write(data)
