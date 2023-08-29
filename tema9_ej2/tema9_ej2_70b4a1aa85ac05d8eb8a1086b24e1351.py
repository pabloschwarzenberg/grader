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
        result = [[0, 0],
                 [0, 0]]
        for i in range(len(self.celdas)): 
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    if self.celdas[0][0] != other.celdas[0][0] or self.celdas[0][1] != other.celdas[0][1]:
                        result[i][j] += self.celdas[i][k] * other.celdas[k][j]
        self.celdas = result
        return self.celdas

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r = a*b
    print(r)
           