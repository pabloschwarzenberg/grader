#Sistema de Ecuaciones
def resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2):
    denominador = a1 * b2 - a2 * b1
    if denominador == 0:
        return None  # El sistema no tiene solución única
    
    x = (c1 * b2 - c2 * b1) / denominador
    y = (a1 * c2 - a2 * c1) / denominador
    return x, y

# Pedir al usuario los coeficientes y el lado derecho de las ecuaciones
a1 = float(input("Coeficiente de x en la primera ecuación: "))
b1 = float(input("Coeficiente de y en la primera ecuación: "))
c1 = float(input("Lado derecho de la primera ecuación: "))

a2 = float(input("Coeficiente de x en la segunda ecuación: "))
b2 = float(input("Coeficiente de y en la segunda ecuación: "))
c2 = float(input("Lado derecho de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
solucion = resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones redondeadas a un decimal
if solucion:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")