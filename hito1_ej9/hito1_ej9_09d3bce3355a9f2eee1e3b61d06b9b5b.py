#Sistema de Ecuaciones
a=float(input("ingrese a:"))
b=float(input("ingrese b:"))
c=float(input("ingrese c:"))
d=float(input("ingrese d:"))
e=float(input("ingrese e:"))
f=float(input("ingrese f:"))
x=(c*e-b*f)/(a*e-b*d)
y=(a*f-c*d)/(a*e-b*d)
print("x=",round(x,1))
print("y=",round(y,1))