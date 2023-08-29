class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.data = [[0] * columnas for _ in range(filas)]

    def __str__(self):
        return '\n'.join([' '.join([str(elemento) for elemento in fila]) for fila in self.data])

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.data[i][j] += self.data[i][k] * otra_matriz.data[k][j]

        return resultado
