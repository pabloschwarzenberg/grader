#Sistema de Ecuaciones
# Obtén los valores del sistema de ecuaciones
a = float(input("Coeficiente de x en la primera ecuación: "))
b = float(input("Coeficiente de y en la primera ecuación: "))
c = float(input("Termino independiente de la primera ecuación: "))
d = float(input("Coeficiente de x en la segunda ecuación: "))
e = float(input("Coeficiente de y en la segunda ecuación: "))
f = float(input("Termino independiente de la segunda ecuación: "))

# Calcula las soluciones del sistema de ecuaciones
denominador = a * e - b * d
if denominador != 0:
    x = (c * e - b * f) / denominador
    y = (a * f - c * d) / denominador
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
      