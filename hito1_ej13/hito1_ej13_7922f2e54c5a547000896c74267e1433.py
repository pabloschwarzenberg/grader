#Factores Primos
import numpy as np
n = int(input("ingrese un numero mayor a 1: "))
primos = []

for i in range(2, n+1):
    while n%i == 0:
        primos.append(i)
        n = n/i
print(np.arrayprimos)