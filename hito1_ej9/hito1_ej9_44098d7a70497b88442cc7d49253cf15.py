#Sistema de Ecuaciones

# Recibimos la entrada del usuario
a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
b1 = float(input("Ingrese el término independiente b1: "))

a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b2 = float(input("Ingrese el término independiente b2: "))

# Calculamos los determinantes de la matriz de coeficientes
detA = a11 * a22 - a12 * a21
detX = b1 * a22 - b2 * a12
detY = a11 * b2 - a21 * b1

# Verificamos si el sistema tiene solución única
if detA != 0:
    # Calculamos las soluciones
    x = detX / detA
    y = detY / detA

    # Imprimimos las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única")
      