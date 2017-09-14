
def summ(a):
    for i in a[r]:
        if i==c:
            return True
        elif i==q:
            return False
a = []
b = 0
c = [['X'],['X'],['X']]
q =[['O'],['O'],['O']]
for r in range(3): # 6 строк
    a.append([]) # создаем пустую строку
    for c in range(3): # в каждой строке - 10 элементов
        import random
        a[r].append(random.choices (["O","X"]))
for t in a:
    print (t)

summ(a)
if summ(a)== True:
    print ("wins X")
elif summ(a)== False:
    print ("wins O")
else:
    print ("Draw")
