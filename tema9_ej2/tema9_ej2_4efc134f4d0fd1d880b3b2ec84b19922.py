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
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("El número de columnas de la matriz izquierda debe ser igual al número de filas de la matriz derecha.")

        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                sum = 0
                for k in range(len(other.celdas)):
                    sum += self.celdas[i][k] * other.celdas[k][j]
                row.append(sum)
            result.append(row)

        return Matriz(result)
