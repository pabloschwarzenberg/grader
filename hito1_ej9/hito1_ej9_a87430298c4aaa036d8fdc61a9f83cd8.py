#Sistema de Ecuaciones
 
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término constante en la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término constante en la segunda ecuación: "))

determinante_principal = a * e - b * d

determinante_x = c * e - b * f
determinante_y = a * f - c * d

x = determinante_x / determinante_principal
y = determinante_y / determinante_principal

print("x =", round(x, 1))
print("y =", round(y, 1))
