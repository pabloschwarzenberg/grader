class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.data = [[0] * columnas for _ in range(filas)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.data])

    def __mul__(self, otra):
        if self.columnas != otra.filas:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = Matriz(self.filas, otra.columnas)

        for i in range(self.filas):
            for j in range(otra.columnas):
                for k in range(self.columnas):
                    resultado.data[i][j] += self.data[i][k] * otra.data[k][j]

        return resultado


if __name__ == "__main__":
    o1 = Matriz(2, 2)
    o1.data = [[1, 2], [3, 4]]

    o2 = Matriz(2, 2)
    o2.data = [[5, 6], [7, 8]]

    resultado = o1 * o2
    print(resultado)

