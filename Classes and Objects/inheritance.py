#Inheritance with overriding
class Parent:
    parent_name=""
    def __init__(self):
        print("Parent Class")
    def printParentName(self):
        print("Parent is",self.parent_name)
    def setName(self,name):
        self.parent_name=name
class Child(Parent):
    child_name=""
    def __init__(self):
        print("Child Class")
    def printChildName(self):
        print("Child is",self.child_name)
    def setName(self,name):
        self.child_name=name
child1=Child();
print(child1.printChildName())
print(child1.printParentName())
child1.setName("Arjun")

print(child1.printChildName())
print(child1.printParentName())

