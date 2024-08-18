from threading import Thread


class Hello(Thread):
    def run(self):
        for i in range(100):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(100):
            print("Hi")

t1=Hello()
t2=Hi()
t1.start()
t1.join()
t2.start()
t2.join()

print("Bye")
