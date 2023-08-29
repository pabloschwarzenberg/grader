def resolver_sistema(a1, b1, c1, a2, b2, c2):
    denominador = a1 * b2 - a2 * b1

    if denominador == 0:
        return None  # El sistema no tiene solución única

    x = round((c1 * b2 - c2 * b1) / denominador, 1)
    y = round((a1 * c2 - a2 * c1) / denominador, 1)

    return x, y

# Ejemplo de uso
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion is None:
    print("El sistema no tiene solución única")
else:
    print("x =", round(solucion[0], 1))
    print("y =", round(solucion[1], 1))
