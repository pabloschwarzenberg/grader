class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0] * columnas for _ in range(filas)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.datos])

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las matrices no son compatibles para multiplicación.")

        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.datos[i][j] += self.datos[i][k] * otra_matriz.datos[k][j]

        return resultado


# Ejemplo de uso
matriz1 = Matriz(2, 3)
matriz1.datos = [[1, 2, 3], [4, 5, 6]]
print("Matriz 1:")
print(matriz1)

matriz2 = Matriz(3, 2)
matriz2.datos = [[7, 8], [9, 10], [11, 12]]
print("\nMatriz 2:")
print(matriz2)

resultado = matriz1 * matriz2
print("\nResultado de la multiplicación:")
print(resultado)
