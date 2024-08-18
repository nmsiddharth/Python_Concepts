
n = int(input("Enter the number: "))
def fib(num):
    f=0
    s=1
    if n==1:
        print(f)
    else :
        print(f)
        print(s)

        for i in range(2,num):
            t=f+s
            f=s
            s=t
            print(t)
fib(n)


