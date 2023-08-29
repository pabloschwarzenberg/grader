class Matriz:
    def __init__(self, matriz):
        self.filas = len(matriz)
        self.columnas = len(matriz[0])
        self.matriz = matriz

    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.matriz])

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = Matriz([[0] * otra_matriz.columnas for _ in range(self.filas)])

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]

        return resultado
