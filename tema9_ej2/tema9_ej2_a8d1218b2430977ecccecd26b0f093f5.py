class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.celdas])

    def __mul__(self, other):
        if len(self.celdas) == 0 or len(other.celdas) == 0:
            return Matriz()

        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("Las matrices no tienen dimensiones compatibles para multiplicación.")

        filas_resultado = len(self.celdas)
        columnas_resultado = len(other.celdas[0])
        result = [[0] * columnas_resultado for _ in range(filas_resultado)]

        for i in range(filas_resultado):
            for j in range(columnas_resultado):
                for k in range(len(other.celdas)):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
