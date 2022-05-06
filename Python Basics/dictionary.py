#
my_dict={"name":"Arjun","Age":22,"place":"Banglore"}
print(my_dict)
print("Name is: ",my_dict['name'])

#Updating Dictionary
my_dict['name']="Amal"
print(my_dict)

#Delete Dictionary Elements
del my_dict['place']
print(my_dict)

my_dict.clear()
print("Dict after clearing",my_dict)

#Built-in Dictionary Functions & Methods
dict1={"name":"Arjun","Age":22,"place":"Banglore"}
dict2={"post_office":"Bglr","YOB":2000}
print(dict1)
print(dict2)
print("The length of dict1",len(dict1))
dict3=dict1.copy()
print(dict3)
print(dict1.items())
print(dict2.values())
dict3.update(dict2)
print(dict3)
