#Sistema de Ecuaciones
print("resolución de dos ecuaciones con dos incógnitas")

print("ejemplo:")
print("a= 2x + 3y=6")
print("b= 1x + 2y=5")

A = int(input("ingrese valor para A: "))
B = int(input("ingrese valor para B: "))
C = int(input("ingrese valor para C: "))
D = int(input("ingrese valor para D: "))
E = int(input("ingrese valor para E: "))
F = int(input("ingrese valor para F: "))

Determinante = A*E - B*D

if Determinante != 0:
    x =(C*E - B*F) / Determinante
    y =(A*F - C*D) / Determinante
    print("x=" +str(x) + "y=" +str(y))

else:
    print("no hay solucion")