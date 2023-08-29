#Sistema de Ecuaciones
# Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    # Resuelve el sistema mediante el método de sustitución
    y = (c - (a * f / d)) / (b - (a * e / d))
    x = (c - (b * y)) / a

    return x, y

# Leer los valores del sistema de ecuaciones
a = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
print("La solución del sistema de ecuaciones es:")
print("x = {:.1f}".format(solucion[0]))
print("y = {:.1f}".format(solucion[1]))
