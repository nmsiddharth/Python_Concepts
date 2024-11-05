
from threading import *
from time import *

def display(str1):
    l.acquire()
    for i in str1:
        print(i)
        sleep(0.7)
    l.release()

l = Semaphore(1)  # Number denotes how many threads can it access at a time
t1 = Thread(target=display,args=("Hello World",))
t2 = Thread(target=display,args=("Welcome",))
t3 = Thread(target=display,args=("0123456",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


