# Recibimos los coeficientes de la primera ecuación
a1 = float(input("Introduce el coeficiente a1: "))
b1 = float(input("Introduce el coeficiente b1: "))
c1 = float(input("Introduce el término independiente c1: "))

# Recibimos los coeficientes de la segunda ecuación
a2 = float(input("Introduce el coeficiente a2: "))
b2 = float(input("Introduce el coeficiente b2: "))
c2 = float(input("Introduce el término independiente c2: "))

# Calculamos el determinante de la matriz de coeficientes
det = a1 * b2 - a2 * b1

# Verificamos si el sistema tiene solución única
if det != 0:
    # Calculamos las soluciones del sistema
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    # Imprimimos las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    # El sistema no tiene solución única
    print("El sistema no tiene solución única")
