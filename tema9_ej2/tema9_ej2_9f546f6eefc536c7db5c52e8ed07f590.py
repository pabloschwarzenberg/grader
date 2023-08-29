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
        if len(self.celdas) == 0 or len(other.celdas) == 0:
            return Matriz()

        filas_self = len(self.celdas)
        columnas_self = len(self.celdas[0])
        filas_other = len(other.celdas)
        columnas_other = len(other.celdas[0])

        if columnas_self != filas_other:
            raise ValueError("No se pueden multiplicar matrices con dimensiones incompatibles.")

        resultado = Matriz([[0] * columnas_other for _ in range(filas_self)])

        for i in range(filas_self):
            for j in range(columnas_other):
                for k in range(columnas_self):
                    resultado.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return resultado

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           