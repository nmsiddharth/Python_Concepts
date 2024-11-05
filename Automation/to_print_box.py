
class Box:
    def boxprint(self,symbol,width,height):

        if len(symbol)!= 1:
            raise Exception("Symbol should be of length 1")

        print(symbol*width)

        for i in range(height):
            print(symbol + (' '*(width-2)) + symbol)

        print(symbol*width)

box = Box()
box.boxprint('**',15,3)