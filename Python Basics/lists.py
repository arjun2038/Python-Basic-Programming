new_list=["arjun","amal","aswin",324,567]
#Accessing Lists
print(new_list[1])
print(new_list[1:3])
print(new_list[-2:])

#Updating Lists
new_list[3]="samsung"
print(new_list)

#Delete List Elements
del new_list[4]
print(new_list)

#Built-in List Functions & Methods

print(len(new_list))
print(tuple(new_list))
new_list.append("first")
print(new_list)
new_list.pop()
print(new_list)
new_list.insert(1,"second")
print(new_list)
new_list.remove("second")
print(new_list)
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)