#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante == 0:
        return None  # El sistema no tiene solución única
    else:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return x, y

# Solicitar los coeficientes al usuario
a = float(input("Coeficiente de x en la primera ecuación: "))
b = float(input("Coeficiente de y en la primera ecuación: "))
c = float(input("Resultado de la primera ecuación: "))
d = float(input("Coeficiente de x en la segunda ecuación: "))
e = float(input("Coeficiente de y en la segunda ecuación: "))
f = float(input("Resultado de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if solucion is None:
    print("El sistema no tiene solución única.")
else:
    x = round(solucion[0], 1)
    y = round(solucion[1], 1)
    print("x =", x)
    print("y =", y)

