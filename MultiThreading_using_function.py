from threading import *
from time import *
def display():
    for i in range(65,91):
        print(chr(i))
        sleep(1)

t = Thread(target=display,name="Alphabets")
t.start()
t.join()
for i in range(65,91):
    print(i)
    sleep(1)



