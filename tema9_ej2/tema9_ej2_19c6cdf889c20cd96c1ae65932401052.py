class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
    
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
        rows_self = len(self.celdas)
        cols_self = len(self.celdas[0])
        rows_other = len(other.celdas)
        cols_other = len(other.celdas[0])

        # Verificar si las matrices se pueden multiplicar
        if cols_self != rows_other:
            raise ValueError("No se pueden multiplicar las matrices")

        # Crear una matriz resultante llena de ceros
        result = Matriz([[0] * cols_other for _ in range(rows_self)])

        # Realizar la multiplicación de matrices
        for i in range(rows_self):
            for j in range(cols_other):
                for k in range(cols_self):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
           