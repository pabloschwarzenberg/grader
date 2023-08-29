#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante
    return x, y


# Lectura de los coeficientes del sistema
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

solucion = resolver_sistema(a, b, c, d, e, f)

if solucion:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
