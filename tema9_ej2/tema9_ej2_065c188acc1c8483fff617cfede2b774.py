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
            print("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        else:
            filas = len(self.celdas)
            columnas = len(other.celdas[0])
            mm = []  # matriz multiplicación
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    suma = 0
                    for k in range(len(self.celdas[0])):
                        suma += self.celdas[i][k] * other.celdas[k][j]
                    fila.append(suma)
                mm.append(fila)
        return Matriz(mm)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)

           