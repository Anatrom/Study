import random
b=[]
a = random.uniform(0,100)
a=int(a)
print(a)
while a < 90:
    b.append(a)
    a = random.uniform(0, 100)
    a = int(a)
else:
     pass
for i in b:
    print (i,'\n')

