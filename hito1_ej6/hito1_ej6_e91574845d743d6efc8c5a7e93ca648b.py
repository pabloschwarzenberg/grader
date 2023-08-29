#Ordenar tres números
a1=int(input("Ingrese un número:"))
b1=int(input("Ingrese otro número porfavor:"))
c1=int(input("Ingrese otro número porfavor:"))
if a1<=b1<=c1:
    print(str(a1)+",",str(b1)+",",str(c1))
elif a1<=c1<=b1:
    print(str(a1)+",",str(c1)+",",str(b1))
elif b1<=c1<=a1:
    print(str(b1)+",",str(c1)+",",str(a1))
elif b1<=a1<=c1:
    print(str(b1)+",",str(a1)+",",str(c1))
elif c1<=a1<=b1:
    print(str(c1)+",",str(a1)+",",str(b1))
elif c1<=b1<=a1:
    print(str(c1)+",",str(b1)+",",str(a1))