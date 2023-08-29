# Solicitar al usuario ingresar los coeficientes y constantes de las ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante de la segunda ecuación: "))

# Calcular las soluciones
det = a1 * b2 - a2 * b1

if det != 0:
    x_sol = round((c1 * b2 - c2 * b1) / det, 1)
    y_sol = round((a1 * c2 - a2 * c1) / det, 1)

    # Imprimir las soluciones
    print("La solución para x es: x =", x_sol)
    print("La solución para y es: y =", y_sol)
else:
    print("El sistema de ecuaciones no tiene solución única.")