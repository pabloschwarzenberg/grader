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
        if len(self.celdas) == 0 or len(self.celdas[0]) == 0 or len(other.celdas) == 0 or len(other.celdas[0]) == 0:
            raise ValueError("Las matrices deben tener elementos para multiplicarse.")
        
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")

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
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)           