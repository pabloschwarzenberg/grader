#Sistema de Ecuaciones
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
d = int(input("Ingrese a': "))
e = int(input("Ingrese b': "))
f = int(input("Ingrese c': "))

deter = a*e -b*d
x = (c*e - b*f)/deter
y = (a*f - c*d)/deter

print('x =' ,x,',','y =', y)
