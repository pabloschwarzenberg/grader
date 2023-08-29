#Sistema de Ecuaciones
a1=float(input("n1= "))
b1=float(input("n2= "))
c1=float(input("n3= "))
a2=float(input("n4= "))
b2=float(input("n5= "))
c2=float(input("n6= "))
if a1/a2==b1/b2 and b1/b2==c1/c2:
    print("la ecuacion tiene infinitas soluciones")
elif a1/a2==b1/b2 and b1/b2 != c1/c2:
    print("la ecuacion no tiene solucion dentro de los reales")
else:
    x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
    y=(a1*c2-a2*c1)/(a1*b2-a2*b1)
    print("x= ",round(x,1))
    x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
    y=(a1*c2-a2*c1)/(a1*b2-a2*b1)
    print("y= ",round(y,1))    