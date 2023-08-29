class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[i])):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("Las matrices no se pueden multiplicar debido a un tamaño incompatible.")

        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                sum = 0
                for k in range(len(self.celdas[0])):
                    sum += self.celdas[i][k] * other.celdas[k][j]
                row.append(sum)
            result.append(row)

        return Matriz(result)


if __name__ == "__main__":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2 = Matriz([[5, 6], [7, 8]])

    resultado = matriz1 * matriz2
    print(resultado)
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           