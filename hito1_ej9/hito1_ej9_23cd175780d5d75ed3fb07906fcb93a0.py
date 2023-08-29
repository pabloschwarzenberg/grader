#Sistema de Ecuaciones
print(" ax+by=c, dx+ey=f ")
a=int(input("Ingrese el coeficiente a: "))
b=int(input("Ingrese el coeficiente b: "))
c=int(input("Ingrese el coeficiente c: "))
d=int(input("Ingrese el coeficiente d: "))
e=int(input("Ingrese el coeficiente e: "))
f=int(input("Ingrese el coeficiente f: "))

x=(-b*f+e*c)/(a*e-b*d)
y=(a*f-d*c)/(a*e-b*d)

print("x= ", round(x,1))
print("y= ", round(y,1))