#Ordenar tres números
n1 = int(input("ingrese el numero: "))
n2 = int(input("ingrese el numero: "))
n3 = int(input("ingrese el numero: "))
if (n1<n2):
    if  (n1<=n3):
        primero=n1
        if  (n2<n3):
            segundo=n2
            tercero=n3
        else:
            segundo=n3
            tercero=n2
    else:
        primero=n3
        segundo=n2
        tercero=n1
else:
    if  (n2<=n3):
        primero=2
        if  (n1<n3):
            segundo=n1
            tercero=n3
        else:
            segundo=n3
            tercero=n1
    else:
        primero=n3
        segundo=n2
        tercero=n1
print(primero,",",segundo,",",tercero)

