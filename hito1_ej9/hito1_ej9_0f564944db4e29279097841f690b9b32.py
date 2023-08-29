#Sistema de Ecuaciones
a=float(input("Ingrese a:"))
b=float(input("Ingrese b:"))
c=float(input("Ingrese c:"))
d=float(input("Ingrese d:"))
e=float(input("Ingrese e:"))
f=float(input("Ingrese f:"))
x=((b*f-e*c)/(b*d-e*a))
y=((a*f-c*d)/(a*e-b*d))
if a*e==b*d:
  print("ERROR")
else:
  print("x=",x)
  print("y=",y)
  print("x=",x,",","y=",y)