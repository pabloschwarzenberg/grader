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
            raise ValueError("Las matrices no son compatibles para la multiplicación.")
 
        result = Matriz([[0] * len(other.celdas[0]) for _ in range(len(self.celdas))])
 
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]
 
        return result
m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
resultado = m1 * m2
print(resultado)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           