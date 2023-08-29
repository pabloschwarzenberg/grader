#Sistema de Ecuaciones
# Pedir al usuario los coeficientes y términos constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término constante de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término constante de la segunda ecuación: "))

# Calcular las soluciones del sistema
denominador = a1 * b2 - a2 * b1

if denominador != 0:
    x = (b2 * c1 - b1 * c2) / denominador
    y = (a1 * c2 - a2 * c1) / denominador
    x = round(x, 1)
    y = round(y, 1)
    print("x =", x)
    print("y =", y)
else:
    print("El sistema no tiene solución única.")      