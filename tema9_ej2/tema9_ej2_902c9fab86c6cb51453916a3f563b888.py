import numpy as np

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las matrices no tienen dimensiones compatibles para la multiplicación")

        resultado = np.dot(self.matriz, otra_matriz.matriz)

        return Matriz(resultado)

    def __str__(self):
        matriz_str = ""
        for fila in self.matriz:
            matriz_str += " ".join(str(elemento) for elemento in fila) + "\n"
        return matriz_str

# Ejemplo de uso
matriz1 = Matriz([[1, 2], [3, 4]])
matriz2 = Matriz([[5, 6], [7, 8]])

resultado = matriz1 * matriz2
print(resultado)