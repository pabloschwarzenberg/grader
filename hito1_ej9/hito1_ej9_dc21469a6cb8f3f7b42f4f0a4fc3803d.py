# Obtener los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))
# Calcular las soluciones del sistema de ecuaciones
det = a1 * b2 - a2 * b1
det_x = c1 * b2 - c2 * b1
det_y = a1 * c2 - a2 * c1
# Comprobar si el sistema tiene solución única
if det != 0:
    x = det_x / det
    y = det_y / det
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema de ecuaciones no tiene una solución única.")