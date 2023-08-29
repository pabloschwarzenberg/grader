class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        m = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                m += "{0: >5} ".format(self.celdas[i][j])
            m += "\n"
        return m

    def __mul__(self, otro):
        if len(self.celdas[0]) != len(otro.celdas):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")

        resultado = Matriz([[0] * len(otro.celdas[0]) for _ in range(len(self.celdas))])

        for i in range(len(self.celdas)):
            for j in range(len(otro.celdas[0])):
                for k in range(len(otro.celdas)):
                    resultado.celdas[i][j] += self.celdas[i][k] * otro.celdas[k][j]

        return resultado

if __name__ == "main":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2= Matriz([[5, 6], [7, 8]])
    matriz3 = matriz1* matriz2
    print(matriz3)
