def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d

    if determinante != 0:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return x, y
    else:
        return None

# Obtener los coeficientes del sistema de ecuaciones del usuario
a = float(input("Ingrese el coeficiente a de la primera ecuación: "))
b = float(input("Ingrese el coeficiente b de la primera ecuación: "))
c = float(input("Ingrese el término independiente c de la primera ecuación: "))
d = float(input("Ingrese el coeficiente d de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente e de la segunda ecuación: "))
f = float(input("Ingrese el término independiente f de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if solucion is not None:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema de ecuaciones no tiene solución única.")
