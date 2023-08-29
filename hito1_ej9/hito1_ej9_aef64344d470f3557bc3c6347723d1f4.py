#Sistema de Ecuaciones
 
a1=float(input("Ingrese el numero que acompaña al x:"))
b1=float(input("Ingrese el numero que acompaña al y:"))
c1=float(input("Ingrese el numero que esta despues de la igualdad:"))

a2=float(input("Ingrese el numero que acompaña al x:"))
b2=float(input("Ingrese el numero que acompaña al y:"))
c2=float(input("Ingrese el numero que esta despues de la igualdad:"))

if b2*a1-b1*a2==0 and c2*a1-c1*a2!=0:
    print("El sistema de ecuaciones no tiene solucion")
elif b2*a1-b1*a2==0 and c2*a1-c1*a2==0:
    print("El sistema de ecuaciones tiene infinitas soluciones")
elif b2*a1-b1*a2!=0:
    y=(a2*c1-a1*c2)/(b1*a2-b2*a1)
    x=(c1/a1)-(b1*(a2*c1-a1*c2))/(a1*(b1*a2-b2*a1))
    print("x="+str(x))
    print("y="+str(y))
