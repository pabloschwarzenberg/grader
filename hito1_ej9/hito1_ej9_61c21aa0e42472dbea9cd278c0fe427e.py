#Sistema de Ecuaciones
a = float (input("Inserte a: "))
b = float (input("Inserte b: "))
c = float (input("Inserte c: "))
d = float (input("Inserte d: "))
e = float (input("Inserte e: "))
f = float (input("Inserte f: "))
D = a*e - b*d
Dx = c*e - f*b
Dy = a*f - d*c
x = Dx / D
y = Dy / D
print("x=",x)
print("y=",y)