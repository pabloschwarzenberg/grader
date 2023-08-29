class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0 for j in range(columnas)] for i in range(filas)]

    def __mul__(self, otra):
        if self.columnas != otra.filas:
            return None

        resultado = Matriz(self.filas, otra.columnas)

        for i in range(self.filas):
            for j in range(otra.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra.matriz[k][j]

        return resultado

matriz1 = Matriz(2, 3)
matriz1.matriz = [[1, 2, 3], [4, 5, 6]]

matriz2 = Matriz(3, 2)
matriz2.matriz = [[7, 8], [9, 10], [11, 12]]

resultado = matriz1 * matriz2