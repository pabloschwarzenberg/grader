#Sistema de Ecuaciones
print("ax + by = c")
print("dx + ey = f")
a = eval(input("ingrese a: "))
b = eval(input("ingrese b: "))
c = eval(input("ingrese c: "))
d = eval(input("ingrese d: "))
e = eval(input("ingrese e: "))
f = eval(input("ingrese f: "))

x = (c*e-f*b)/(a*e-b*d)
y = (a*f-d*c)/(a*e-b*d)

print("x=",x)
print("y=",y)
