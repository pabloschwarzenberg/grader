class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = []
        for i in range(len(self.celdas)):
            fila = []
            for j in range(len(other.celdas[0])):
                valor = 0
                for k in range(len(other.celdas)):
                    valor += self.celdas[i][k] * other.celdas[k][j]
                fila.append(valor)
            resultado.append(fila)

        return Matriz(resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)

           