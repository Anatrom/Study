i = int( input () )  # It is a number
a = i
nloops = 0  # it is cout of loops#
while nloops < 100:
    print(a)
    a = (a+i//a) // 2
    nloops += 1
print(a)  # it is closest int.number that **2<= first number