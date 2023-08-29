print("resolucion de dos ecuaciones con dos incognitas")

print("ejemplo:")
print("a= 2x + 3y=6")
print("b= 1x + 2y=5")

A = int(input("ingrese valor para A: "))
B = int(input("ingrese valor para B: "))
C = int(input("ingrese valor para C: "))
D = int(input("ingrese valor para D: "))
E = int(input("ingrese valor para E: "))
F = int(input("ingrese valor para F: "))

m = A*E
n = B*D
p = C*E
l = B*F
o = A*F
q = C*D


determinante = m - n

if determinante != 0:
    x =(p - l) / determinante
    y =(o - q) / determinante
    print("x=" +str(x) + "y=" +str(y))

else:
    print("no hay solucion")
