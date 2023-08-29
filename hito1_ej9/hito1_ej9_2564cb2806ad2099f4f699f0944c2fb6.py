#Sistema de Ecuaciones
a=float(input("Ingrese coeficiente de X1:"))
b=float(input("Ingrese coeficiente de Y1:"))
c=float(input("Ingrese resultado1:"))
d=float(input("Ingrese coeficiente de X2:"))
e=float(input("Ingrese coeficiente de Y2:"))
f=float(input("Ingrese resultado2:"))
if((a/b)!=(d/e)):
    p=b*d/a-e
    q=c*d/a-f
    y=q/p
    x=(c-y*b)/a
    y=round(y,1)
    x=round(x,1)
    print("x="+str(x))
    print("y="+str(y))
else:
    print("El sistema tiene infinitas soluciones, o no tiene")