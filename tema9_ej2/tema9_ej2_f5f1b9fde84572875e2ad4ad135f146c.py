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
        if len(self.celdas) == 0 or len(self.celdas) != len(other.celdas[0]):
            raise ValueError("Las dimensiones de las matrices no son válidas para la multiplicación")

        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                cell_value = 0
                for k in range(len(other.celdas)):
                    cell_value += self.celdas[i][k] * other.celdas[k][j]
                row.append(cell_value)
            result.append(row)

        return Matriz(result)


# Ejemplo de uso
m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
m3 = m1 * m2
print(m3)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           