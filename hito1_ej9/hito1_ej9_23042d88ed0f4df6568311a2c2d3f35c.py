# Obtener los coeficientes y resultados del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

# Calcular determinante
determinante = a1 * b2 - a2 * b1

# Verificar si el sistema tiene solución única
if determinante != 0:
    # Calcular soluciones
    solucion_x = (b2 * c1 - b1 * c2) / determinante
    solucion_y = (a1 * c2 - a2 * c1) / determinante

    # Imprimir las soluciones redondeadas a un decimal
    solucion_x = round(solucion_x, 1)
    solucion_y = round(solucion_y, 1)

    print("La solución del sistema de ecuaciones es:")
    print("x =", solucion_x)
    print("y =", solucion_y)
else:
    print("El sistema de ecuaciones no tiene solución única.")
