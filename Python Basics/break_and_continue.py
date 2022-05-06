#break using program
print("break using program")
for i in range(1,10):
    print(i)
    if(i%5==0):
        break

#continue using program
print("continue using program")
for i in range(1,10):
    if (i % 2 == 0):
        continue
    print(i)
