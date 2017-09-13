def notnumber(h):
    if h.isalpha():
        return True
    else:
        return False

while (1):
    h = input("текст")
    h=h.lower()
    k=sorted(h)
    print (k)
    notnumber(h)
    test=[]
    if notnumber(h)== True:

        import string
        h.split()
        for i in h:
            if h.count(i)>1:
                test.append(i)
        print (test)
        y = tuple(test)
        a=max(y)
        print (a)
    else:
        print ('Вы используете не текст')
