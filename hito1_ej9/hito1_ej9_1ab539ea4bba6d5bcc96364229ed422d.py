#Sistema de Ecuaciones
print("Ingresa los valores solicitados. Estos representan ecuaciones de la forma: ax+by=e y cx+dy=f")
a=float(input("ingrese a:"))
b=float(input("ingrese b:"))
e=float(input("ingrese e:"))
c=float(input("ingrese c:"))
d=float(input("ingrese d:"))
f=float(input("ingrese f:"))
det = a*d-b*c 
x= (e*d-f*b)/det
y= (a*f-c*e)/det
print("x=", x)
print("y=", y)  