#Sistema de Ecuaciones
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
d = int(input("Ingrese d: "))
e = int(input("Ingrese e: "))
f = int(input("Ingrese f: "))

dis = (a*e - b*d)
x2 = (f*a - d*c)/dis
x1 = (c - b*x2)/a
print("x=", round(x1,1), "y=", round(x2,1))