"""
2.- La suma de los primeros n numeros naturales está dada por n(n + 1)/2.
Crea un programa que reciba como parámetro un número N y luego imprima la suma
de los N primeros números naturales
"""

N = int(input("Cantidad de números: "))

for n in range(1, N+1):
    suma = (n*(n + 1))/2
    print(suma)
      