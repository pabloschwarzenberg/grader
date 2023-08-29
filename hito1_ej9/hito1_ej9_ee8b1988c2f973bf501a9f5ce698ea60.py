def resolver_sistema(a, b, c, d, e, f):
    # Calcular determinante
    determinante = a * d - b * c

    if determinante == 0:
        # El sistema no tiene solución única
        return None
    else:
        # Calcular soluciones
        x = (e * d - b * f) / determinante
        y = (a * f - c * e) / determinante
        return x, y

# Solicitar los coeficientes del sistema al usuario
a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c = float(input("Ingrese el coeficiente 'c' de la segunda ecuación: "))
d = float(input("Ingrese el coeficiente 'd' de la segunda ecuación: "))
e = float(input("Ingrese el término independiente 'e' de la primera ecuación: "))
f = float(input("Ingrese el término independiente 'f' de la segunda ecuación: "))

# Resolver el sistema
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir resultados
if solucion is not None:
    x, y = solucion
    print("x={round(x, 1)}")
    print("y={round(y, 1)}")
else:
    print("El sistema no tiene solución única.")

