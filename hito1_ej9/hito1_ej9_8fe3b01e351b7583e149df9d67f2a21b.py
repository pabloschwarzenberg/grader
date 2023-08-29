#Sistema de Ecuaciones
#ax + by = c
#dx + ey = f

a = float(input("ingrese un a:"))
b = float(input("ingrese un b:"))
c = float(input("ingrese un c:"))
d = float(input("ingrese un d:"))
e = float(input("ingrese un e:"))
f = float(input("ingrese un f:"))
x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)
print("x=",x)
print("y=",y)