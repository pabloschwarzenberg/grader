#Suma de los N primeros números
import math
n = eval(input("Suma de los primeros N numeros naturales. Ingrese N:"))
s = n*(n+1)/2
if n<0:
    print("ingrese un número mayor o igual a 0")
else:
    print(s)
      