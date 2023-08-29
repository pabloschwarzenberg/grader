#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante

    return x, y

# Ejemplo de uso
a = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

solucion = resolver_sistema(a, b, c, d, e, f)
if solucion is None:
    print("El sistema no tiene solución única.")
else:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
