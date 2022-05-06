#operator Overloading by greater

class NewClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __gt__(self, other):
        if(self.a+self.a>self.b+self.b):
            return True
        else:
            return False

new_class1=NewClass(3,5)
new_class2=NewClass(6,1)
if(new_class1>new_class2):
    print("new class1 is greater")
else:
    print("new class2 is greater")
