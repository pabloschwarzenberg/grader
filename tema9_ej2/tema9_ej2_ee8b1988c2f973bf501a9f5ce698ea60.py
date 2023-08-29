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
            raise ValueError("Las matrices no son compatibles para la multiplicación")

        filas_self = len(self.celdas)
        columnas_self = len(self.celdas[0])
        filas_other = len(other.celdas)
        columnas_other = len(other.celdas[0])

        resultado = [[0] * columnas_other for _ in range(filas_self)]

        for i in range(filas_self):
            for j in range(columnas_other):
                suma = 0
                for k in range(columnas_self):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                resultado[i][j] = suma

        return Matriz(resultado)

# Ejemplo de uso
m1 = Matriz([[1, 2, 3], [4, 5, 6]])
m2 = Matriz([[7, 8], [9, 10], [11, 12]])

resultado = m1 * m2
print(resultado)
