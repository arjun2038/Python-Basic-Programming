from math import pi


class Calculations:
    def area(self,a=None,b=None):
        if(a != None and b!=None):
            print("Area of Rectangle", a * b)
        elif(a!=None):
            print("Area of Circle is:", pi * a * a)
        else:
            print("Area Cannot be found")

calc=Calculations()


# calc.area()
calc.area()
