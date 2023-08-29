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
        mm = []
        for i in range(len(self.celdas)):
            f = []
            for j in range(len(other.celdas[0])):
                s = 0
                for k in range(len(other.celdas)):
                    s += self.celdas[i][k] * other.celdas[k][j]
                f.append(s)
            mm.append(f)
        return Matriz(mm)
                    
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           