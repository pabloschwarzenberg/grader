#múltiplos
n1=int(input("ingrese numero:  "))
n2=int(input("ingrese numero mas grande :  "))
while n1<=n2:
    m1=n1%2
    m2=n1%7
    if m1==0 and m2==0:
        print(n1)
    n1=n1+1      