import random as rd
def Abacus_Practice():
    a = rd.randrange(60,69)
    b = rd.randrange(1,10)
    c = rd.randrange(-9,0)
    d = rd.randrange(1,10)
    print(a)
    print('',b)
    print(c)
    print('',d)
    input()
    y =a+b+c+d
    print(y)
    input()
for i in range(25):
    Abacus_Practice()