class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]

    def __str__(self):
        matriz_str = ""
        for fila in self.matriz:
            matriz_str += " ".join(str(elemento) for elemento in fila)
            matriz_str += "\n"
        return matriz_str

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")

        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]

        return resultado
