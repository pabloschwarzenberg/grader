# Pedir al usuario que ingrese los seis números que representan el sistema
a = float(input("Ingresa el coeficiente de x en la primera ecuación: "))
b = float(input("Ingresa el coeficiente de y en la primera ecuación: "))
c = float(input("Ingresa el término independiente de la primera ecuación: "))
d = float(input("Ingresa el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingresa el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingresa el término independiente de la segunda ecuación: "))

# Calcular el determinante del sistema
det = a * e - b * d

# Si el determinante es cero, el sistema no tiene solución única
if det == 0:
  print("El sistema no tiene solución única")
else:
  # Aplicar la regla de Cramer para hallar las soluciones
  x = (c * e - b * f) / det
  y = (a * f - c * d) / det
  # Imprimir las soluciones redondeadas a un decimal
  print("x =", round(x, 1))
  print("y =", round(y, 1))
