import math


def isdigit():
        try:
            int(p)
            return True
        except ValueError:
            return False


p = input("input your value of degres ")

isdigit()
if isdigit():
    p = int(p)
    p = p/360 * 2 * math.pi  # translation digres to radians
    h = round(math.cos(p), 2)  # cosinus
    g = round(math.sin(p), 2)  # sinus
    if h != 0:
        c = round(math.tan(p), 2)
        print('tg', c)
    if g != 0:
        t = round(h/g, 2)
        print('ctg', t)
    print('cos', h,)
    print('sin', g,)
else:
    print("Are you fool? It is not number!!!")
