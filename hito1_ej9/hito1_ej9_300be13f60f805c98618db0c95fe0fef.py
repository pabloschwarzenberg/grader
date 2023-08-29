# Solicitar los coeficientes del sistema al usuario
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término independiente en la primera ecuación: "))

d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término independiente en la segunda ecuación: "))

# Calcular las soluciones
determinante = a * e - b * d

if determinante == 0:
    print("El sistema no tiene solución única.")
else:
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    print("x =", round(x, 1))
    print("y =", round(y, 1))
