import random
M = random.randint(1,101)

def generar_matriz(m, n):
    return[[M for j in range(n)]for i in range(m)]

filas = int(input("Digite la cantidad de filas: "))
columnas = int(input("Digite la cantidad de columnas: "))

matriz = generar_matriz(filas, columnas)

print(matriz)