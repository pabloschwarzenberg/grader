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
        self.mult = [["",""],["",""]]
        self.mult[0][0] = int(self.celdas[0][0]) * int(other.celdas[0][0])
        self.mult[0][1] = int(self.celdas[0][1]) * int(other.celdas[1][0])
        self.mult[1][0] = int(self.celdas[1][0]) * int(other.celdas[0][1])
        self.mult[0][1] = int(self.celdas[1][1]) * int(other.celdas[1][1])
        return self.mult

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(a)
    print(r)
