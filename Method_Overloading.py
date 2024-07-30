class Student:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a + b)
        else:
            print(a)
s1 = Student()
s1.add(2,3,5)