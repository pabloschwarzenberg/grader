#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcular las variables de sustitución
    y = (c1 - a1 * c2 / a2) / (b1 - a1 * b2 / a2)
    x = (c1 - b1 * y) / a1
    
    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))

# Obtener los coeficientes y términos constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término constante en la segunda ecuación: "))

# Resolver el sistema
resolver_sistema(a1, b1, c1, a2, b2, c2)      