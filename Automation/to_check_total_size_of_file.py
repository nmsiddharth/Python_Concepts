import os

totalSize = 0

for filename in os.listdir('D:\\SIDDU\\Resume'):
    if not os.path.isfile(os.path.join('D:\\SIDDU\\Resume',filename)):
        continue
    totalSize += os.path.getsize(os.path.join('D:\\SIDDU\\Resume',filename))

print(totalSize)