def resolver_sistema(a, b, c, d, e, f):
    denominador = a * e - b * d
    if denominador == 0:
        return None  # El sistema no tiene solución única

    x = (c * e - b * f) / denominador
    y = (a * f - c * d) / denominador
    return x, y

# Ingreso de los coeficientes del sistema
a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c = float(input("Ingrese el término independiente 'c' de la primera ecuación: "))
d = float(input("Ingrese el coeficiente 'd' de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente 'e' de la segunda ecuación: "))
f = float(input("Ingrese el término independiente 'f' de la segunda ecuación: "))

# Resolución del sistema
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is not None:
    x_solucion = round(soluciones[0], 1)
    y_solucion = round(soluciones[1], 1)
    print("x =", x_solucion)
    print("y =", y_solucion)
else:
    print("El sistema no tiene solución única.")

