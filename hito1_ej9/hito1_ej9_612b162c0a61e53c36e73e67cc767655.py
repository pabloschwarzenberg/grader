#Sistema de Ecuaciones
print("ax+by=c")
print("dx+ey=f")
a=float(input("ingrese a:"))
b=float(input("ingrese b:"))
c=float(input("ingrese c:"))
d=float(input("ingrese d:"))
e=float(input("ingrese e:"))
f=float(input("ingrese f:"))

y=print("y=",((a*f-d*c)/(a*e-b*d)))
x=print("x=",((f-e*((a*f-d*c)/(a*e-b*d))))/d)
