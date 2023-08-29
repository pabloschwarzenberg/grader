#Sistema de Ecuaciones
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
c=int(input("Ingrese un número: "))
d=int(input("Ingrese un número: "))
e=int(input("Ingrese un número: "))
f=int(input("Ingrese un número: "))



if e*a-d*b!=0 and a!=0:
    x1=((c-b*((a*f-d*c)/(e*a-d*b)))/a)
    y1=(a*f-d*c)/(e*a-d*b)
    print("x=",round(x1,1))
    print("y=",round(y1,1))

else:
    print("x=",round((f-(e*(c/b))/d),1))
    print("y=",round(c/b,1))