#Sistema de Ecuaciones
from math import *
print("ingresar los valores de ecuacion")
B = float(input("ingrese valor de B:"))
A = float(input("ingrese valor de A:"))
C = float(input("ingrese valor de C:"))
disc = (B**2)-(4*A*C)

if disc >= 0:
  raiz1 = ((-B + (SQRT(disc)))/(2A))
  raiz2 = ((-B - (SQRT(disc)))/(2A))
  print("la primera raiz es: ", (raiz1, (round,1))
  print("la segunda raiz es: ", (raiz2, (round,1))
 
  