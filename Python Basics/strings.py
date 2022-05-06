first_name= "Arjun V Pankajakshan"
last_name="VP"
#Accessing Values in Strings

print("name[6]=", first_name[6])
print("name[3:9]=", first_name[3:9])
print("name[:5]=", first_name[:5])
print("name[-1]=", first_name[-1])
print("name[-12:]=", first_name[-12:])

#String Special Operators
print(first_name + last_name) #Concatenation
print(last_name*2) #Repetition

#Membership
for letter in first_name:
    if letter=="a":
        print("Yes")
if "X" not in last_name:
    print("No")

#Updating Strings
print(first_name[:7] + ' P')

#String Formatting Operator
print("I am %s.I am %d years old"%("Arjun",22))


#Built-in String Methods
middle_name="vsp"
print()

#string modification using built in functions
middle_name="Banglore"
print(middle_name.capitalize())
print(middle_name.count('a'))
print(middle_name.isdigit())
print(middle_name.lower())
print(len(middle_name))
print(middle_name.replace("g","@"))

