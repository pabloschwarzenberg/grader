#Sistema de Ecuaciones
print("primera ecuación:")
a1=int(input("ingresa el coeficiente de x:"))
b1=int(input("ingresa el coeficiente de y:"))
c1=int(input("ingresa el coeficiente de posición:"))
print("segunda ecuación:")
a2=int(input("ingresa el coeficiente de x:"))  
b2=int(input("ingresa el coeficiente de y:"))
c2=int(input("ingresa el coeficiente de posición:"))
if (a1*b2)-(a2*b1)!=0 and (a2*b1)-(b2*a1)!=0:
    x = int((c2*b1)-(b2*c1))/((a2*b1)-(b2*a1))
    y = int((a1*c2)-(a2*c1))/((a1*b2)-(a2*b1))
    print("x=",x)
    print("y=",y)
else:
    print("no existe solución")     