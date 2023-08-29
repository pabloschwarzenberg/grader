#Sistema de Ecuaciones
print("ax+by=c")
print("dx+ey=f")
a=float(input("ingrese a:"))
b=float(input("ingrese b:"))
c=float(input("ingrese c:"))
d=float(input("ingrese d:"))
e=float(input("ingrese e:"))
f=float(input("ingrese f:"))

y=(f*a-d*c)/(a*e-d*b)
x=(c-b*y)/a

print("x=" ,x)
print("y=" ,y)