import numpy as np
x1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
y1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
total1 = float(input("Ingrese el resultado de la primera ecuación: "))

x2 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
y2 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
total2 = float(input("Ingrese el resultado de la primera ecuación: "))

variables = np.array([[x1, y1], [x2, y2]])
total = np.array([total1,total2])

solucion = np.linalg.solve(variables, total)

print("x =", round(sol[0], 1))
print("y =", round(sol[1], 1))