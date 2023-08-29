#Sistema de Ecuaciones
print("Dada una ecuación ax+by=c, ingrese los a,b,c de cada ecuación acontinuación")
a1=float(input("Ingrese coeficiente 'a' de la primera ecuación: "))
b1=float(input("Ingrese coeficiente 'b' de la primera ecuación: "))
c1=float(input("Ingrese coeficiente 'c' de la primera ecuación: "))
a2=float(input("Ingrese coeficiente 'a' de la segunda ecuación: "))
b2=float(input("Ingrese coeficiente 'b' de la segunda ecuación: "))
c2=float(input("Ingrese coeficiente 'c' de la segunda ecuación: "))
if a1*b2-a2*b1!=0 and b1*a2-b2*a1!=0:
    y1=(a1*c2-a2*c1)/(a1*b2-a2*b1)
    x1=(c2*b1-b2*c1)/(b1*a2-b2*a1)
    print("x=",x1)
    print("y=",y1)
else:
    print("No está definido")