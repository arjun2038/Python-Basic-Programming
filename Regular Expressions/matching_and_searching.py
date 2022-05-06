import re

#Matching
line="My name is Arjun"
matchObj=re.match(r'is',line,re.M|re.I)
if matchObj:
    print(matchObj.group())
else:
    print("no match found")

#Searching
matchObj=re.search(r'is',line,re.M|re.I)
if matchObj:
    print(matchObj.group())
else:
    print("no match found")
val=re.sub(r'is','are',line)
print(val)

#Search and Replace
phone = "2004-959-559 # This is Phone Number"
ph=re.sub(r'#.*$',"",phone)
print(ph)
ph1=re.sub(r'-',"",ph)
ph2=re.sub(r'\D',"",ph)
print(ph1)
print(ph2)
