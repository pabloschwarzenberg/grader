#Sistema de Ecuaciones
import math
print("Ecuacion cuadratica")
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))
x1= 0
x2= 0

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+math.sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-math.sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print("x=",x1)
  print("y=",x2)
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))
x1= 0
x2= 0

if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+math.sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-math.sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print("x=",x1)
  print("y=",x2)  