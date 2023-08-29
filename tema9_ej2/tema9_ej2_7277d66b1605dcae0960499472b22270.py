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
        if isinstance(other, Matriz):
            if len(self.celdas[0]) != len(other.celdas):
                raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
            
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
        else:
            raise TypeError("El operando no es una instancia de la clase Matriz")

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
