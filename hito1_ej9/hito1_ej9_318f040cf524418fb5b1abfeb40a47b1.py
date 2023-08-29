#Sistema de Ecuaciones
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

determinante = a1 * b2 - a2 * b1
if determinante == 0:
    print("El sistema no tiene solución")
else:
    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    print("Las soluciones son:")
    print("x =", round(x, 1))
    print("y =", round(y, 1))