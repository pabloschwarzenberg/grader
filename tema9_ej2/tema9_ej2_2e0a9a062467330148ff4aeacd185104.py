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
            raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no coinciden.")

        
        result = Matriz([[0] * len(other.celdas[0]) for _ in range(len(self.celdas))])

        
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result
           