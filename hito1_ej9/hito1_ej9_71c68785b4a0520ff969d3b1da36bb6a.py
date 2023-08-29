#Sistema de Ecuaciones
a1 = float(input("Ingrese el x en la primera ecuación: "))
b1 = float(input("Ingrese el y en la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))

a2 = float(input("Ingrese el x en la segunda ecuación: "))
b2 = float(input("Ingrese el y en la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

det = a1 * b2 - a2 * b1

if det== 0:
    print("El sistema no tiene solución única.")
else:
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det

    print("x =", round(x, 1))
    print("y =", round(y, 1))       