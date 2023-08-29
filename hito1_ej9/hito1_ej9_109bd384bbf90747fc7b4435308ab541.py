#Obtener los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

#Calcular las soluciones del sistema de ecuaciones
det = a1 * b2 - a2 * b1

if det == 0:
    print("El sistema de ecuaciones no tiene solución única.")
else:
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det

    # Redondear las soluciones a un decimal
    x = round(x, 1)
    y = round(y, 1)

    # Imprimir las soluciones
    print("x =", x)
    print("y =", y)