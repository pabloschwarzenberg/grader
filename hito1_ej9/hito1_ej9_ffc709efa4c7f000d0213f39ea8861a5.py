print("resolucion de dos ecuaciones con dos incognitas")

print("ejemplo:")
print("a= 2x + 3y=6")
print("b= 1x + 2y=5")

T = int(input("ingrese valor para A: "))
B = int(input("ingrese valor para B: "))
C = int(input("ingrese valor para C: "))
L = int(input("ingrese valor para D: "))
V = int(input("ingrese valor para E: "))
F = int(input("ingrese valor para F: "))

determinante = T*V - B*L

if determinante != 0:
    x =(C*V - B*F) / determinante
    y =(T*F - C*L) / determinante
    print("x=" +str(x) + "y=" +str(y))

else:
    print("no hay solucion")  