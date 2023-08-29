# Ingresar los coeficientes y términos constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término constante en la segunda ecuación: "))

# Calcular las soluciones del sistema de ecuaciones
det = a1 * b2 - a2 * b1
det_x = c1 * b2 - c2 * b1
det_y = a1 * c2 - a2 * c1

# Verificar si el sistema tiene solución o no
if det == 0:
    print("El sistema de ecuaciones no tiene solución.")
else:
    # Calcular las soluciones x e y redondeadas a un decimal
    x = round(det_x / det, 1)
    y = round(det_y / det, 1)
    
    print("x =", x)
    print("y =", y)
