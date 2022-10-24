import math
def f(x):
    return 4*math.e**(-x/2)-x

def fturev(x):
    return -2*math.e**(-x/2)-1

baslangic=float(input("sayi "))
iterasyon=int(input("i.t "))
k=1
x=baslangic
while(k<=iterasyon):
    formul=x-(f(x)/fturev(x))
    print(f"{formul}")
    k=k+1
    x=formul