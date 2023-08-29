class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]

     def __mul__(self, otra_matriz):
         if self.columnas != otra_matriz.filas:
             raise ValueError("Las matrices no se pueden multiplicar")

         resultado = Matriz(self.filas, otra_matriz.columnas)

         for i in range(self.filas):
             for j in range(otra_matriz.columnas):
                 suma = 0
                 for k in range(self.columnas):
                     suma += self.matriz[i][k] * otra_matriz.matriz[k][j]
                 resultado.matriz[i][j] = suma

         return resultado
# Crear la primera matriz 2x3
m1 = Matriz(2, 3)
m1.matriz = [[1, 2, 3], [4, 5, 6]]

# Crear la segunda matriz 3x2
m2 = Matriz(3, 2)
m2.matriz = [[7, 8], [9, 10], [11, 12]]

# Multiplicar las dos matrices
resultado = m1 * m2

# Imprimir el resultado
for fila in resultado.matriz:
    print(fila)
