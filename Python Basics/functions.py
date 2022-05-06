#Defining a Function
def printName(str):
    print(str)

#Calling a Function
printName("Hello World")

#Pass by reference vs value

#Example-1
def modList(new_list):
    new_list.append("Amal")
    print("list inside function is",new_list)
new_list=[1,3,4,'ARJUN']
modList(new_list)
print("list outside function is",new_list)

#Example-2
def modList2(new_list):
    new_list=[1,2,3]
    print("list inside function is", new_list)
new_list=[1,3,4]
modList2(new_list)
print("list outside function is",new_list)

#Default arguments
def defaultArgument(name="Arjun"):
    print("Name is",name)
defaultArgument()
defaultArgument(name="Nihal")

#Variable-length arguments
print("\nVariable-length arguments")
def variableArgument(name,*others):
    print("Name is",name)
    for valu in others:
        print("Name is", valu)
variableArgument("Nihal","Arjun","Amal","Brahmman")

#Anonymous function
print('\n#Anonymous function')
multiply=lambda a,b:a*b
print(multiply(2,3))

#The return Statement
print("\n#The return Statement")
def sample(a,b):
    return a+b;
print("The sum is",sample(3,5))