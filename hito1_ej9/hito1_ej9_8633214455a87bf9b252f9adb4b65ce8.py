#Sistema de Ecuaciones
a = int(input("ingrese numero:"))
b = int(input("ingrese numero:"))
c = int(input("ingrese numero:"))
d = int(input("ingrese numero:"))
e = int(input("ingrese numero:"))
f = int(input("ingrese numero:"))

xy = (a*e - b*d)
x = (c*e - b*f / xy)
y = (a*f - c*d/xy)

print("x =",x)
print("y =",y)
     