#Sistema de Ecuaciones
# Obtener los coeficientes del sistema de ecuaciones
a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
b1 = float(input("Ingrese el término independiente b1: "))

a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b2 = float(input("Ingrese el término independiente b2: "))

# Calcular las soluciones del sistema de ecuaciones
det = a11 * a22 - a12 * a21

if det == 0:
    print("El sistema no tiene solución única")
else:
    x = (b1 * a22 - b2 * a12) / det
    y = (b2 * a11 - b1 * a21) / det

    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
