def resolver_sistema(a, b, c, d, e, f):
    denominador = a * e - b * d
    if denominador == 0:
        return None  # El sistema no tiene solución única
    
    x = (c * e - b * f) / denominador
    y = (a * f - c * d) / denominador
    return (x, y)

# Solicitar los coeficientes del sistema al usuario
a = float(input("Ingrese el coeficiente a de la primera ecuación: "))
b = float(input("Ingrese el coeficiente b de la primera ecuación: "))
c = float(input("Ingrese el término independiente c de la primera ecuación: "))
d = float(input("Ingrese el coeficiente d de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente e de la segunda ecuación: "))
f = float(input("Ingrese el término independiente f de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    print("x=", round(soluciones[0], 1))
    print("y=", round(soluciones[1], 1))