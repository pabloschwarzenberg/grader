#Sistema de Ecuaciones
#2x + 3y = 6
#x + 2y = 5
import numpy as np



x1 = float(input("Ingrese X1"))
y1 = float(input("Ingrese Y1"))
r1 = float(input("Ingrese R1"))
x2 = float(input("Ingrese X2"))
y2 = float(input("Ingrese Y2"))
r2 = float(input("Ingrese R2"))

a = np.array([[x1, y1], [x2, y2]])
b = np.array([r1, r2])
solucion = np.linalg.solve(a, b)
x = ("{:.1f}".format(solucion[0]))
y = ("{:.1f}".format(solucion[1]))
print("x=" + str(x))
print("y=" + str(y))
