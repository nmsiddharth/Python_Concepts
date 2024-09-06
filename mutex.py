
from threading import *
from time import *

def display(str1):
    l.acquire()
    for i in str1:
        print(i)
        sleep(0.7)
    l.release()

l = Lock()
t1 = Thread(target=display,args=("Hello World",))
t2 = Thread(target=display,args=("Welcome",))

t1.start()
t2.start()

t1.join()
t2.join()



