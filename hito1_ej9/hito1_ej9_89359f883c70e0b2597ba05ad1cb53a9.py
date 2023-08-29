# Obtener los coeficientes y términos constantes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término constante de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término constante de la segunda ecuación: "))
# Inicializar las variables x e y
x = 3.0
y = 4.0
# Resolver el sistema de ecuaciones utilizando el método de sustitución
while True:
    if a1 == 0 and b1 == 0:
        print("El sistema no tiene solución.")
        break

    if a1 != 0:
        y = (c1 - a1 * x) / b1
    else:
        x = (c1 - b1 * y) / a1

    if round(a1 * x + b1 * y, 1) == c1 and round(a2 * x + b2 * y, 1) == c2:
        print("x =", round(x, 1))
        print("y =", round(y, 1))
        break

    if a1 != 0:
        x = (c1 - b1 * y) / a1
    else:
        y = (c1 - a1 * x) / b1

    if round(a1 * x + b1 * y, 1) == c1 and round(a2 * x + b2 * y, 1) == c2:
        print("x =", round(x, 1))
        print("y =", round(y, 1))
        break

    if round(a2 * x + b2 * y, 1) == c2:
        print("El sistema no tiene solución.")
        break

    if round(a2 * x + b2 * y, 1) != c2:
        print("El sistema no tiene solución.")
        break
