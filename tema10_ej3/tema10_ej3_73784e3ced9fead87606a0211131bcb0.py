import numpy as np
import random

palabras = ["campo", "arado", "caballo", "vaca", "oveja", "tractor", "semilla"]
DIM = 10
matriz = Matrix(DIM)
while matriz.libres:
    palabra = palabras[random.randint(0, len(palabras) - 1)]
    largo = len(palabra)
    matriz.put(palabra)

print(matriz)
print(matriz.palabras)