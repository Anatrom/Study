while(1):
    mlist=[]
    h=input("число ")
    def digit(h):
        try:
            float(h)
            return True        
        except ValueError:
            return False
    if digit(h)==True:
        mlist.append(h)
    else: print("Цэ не число")
    while h!="end":
        h=input("число ")
        if digit(h)==True:
            mlist.append(h)
        else: print("Цэ не число")     
        print(mlist)
    if 0<=len(mlist)<=10:
        a=min(mlist)
        print ("min",a)
        b=max(mlist)
        print ("max",b)
        print ("your list",mlist)
    result=[]
    for i in mlist:
        if i not in result:
            result.append(i)
    print ("result list",result)
    result1=[]
    for i in mlist:
        if i.count>1:
            result1.append (i)
    
    
    print("result list number 2",result1)
            
            
        
        
