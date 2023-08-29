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
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = []
        for i in range(len(self.celdas)):
            fila_resultado = []
            for j in range(len(other.celdas[0])):
                suma = 0
                for k in range(len(self.celdas[0])):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)

        return Matriz(resultado)
