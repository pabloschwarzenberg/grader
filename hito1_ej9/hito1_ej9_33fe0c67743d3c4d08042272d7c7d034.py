#Sistema de Ecuaciones
## ENTRADA DE DATOS - PROCESO - SALIDA

a1 = float(input("Ingrese el valor de a1: "))
b1 = float(input("Ingrese el valor de b1: "))
c1 = float(input("Ingrese el valor de c1: "))
a2 = float(input("Ingrese el valor de a2: "))
b2 = float(input("Ingrese el valor de b2: "))
c2 = float(input("Ingrese el valor de c2: "))

Determinante = a1 * b2 - a2 * b1

if Determinante == 0:
    print("El sistema de ecuaciones no tiene solución única.")
else:
    x = (c1 * b2 - c2 * b1) / Determinante
    y = (a1 * c2 - a2 * c1) /Determinante

print("x =",round(x, 1))
print("y =",round(y, 1))     