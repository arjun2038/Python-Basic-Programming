import re


sentence="Screening cum selection numerical process for the posts reported vide far notification number KTU/ASST4(ADMIN)/2252/2021 dated 07.02.2022 and 09.03.2022"
print(re.findall(r'[a-c]',sentence))
print(re.findall(r'\d',sentence))
print(re.findall(r'\D',sentence))
print(re.findall(r'f.r',sentence))
va=re.findall(r'^Sc',sentence)
if va:
    print("Yes")
else:
    print("No")
sa=re.findall(r'22$',sentence)
if sa:
    print("Yes")
else:
    print("No")