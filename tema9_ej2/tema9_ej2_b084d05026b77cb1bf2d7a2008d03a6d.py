class Matriz:
    def __init__(self,celdas = []):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        m = []
        f1 = []
        f2 = []
        s1 = (self.celdas[0][0])*(other.celdas[0][0]) + (self.celdas[0][1])*(other.celdas[1][0])
        s2 = (self.celdas[0][0])*(other.celdas[0][1]) + (self.celdas[0][1])*(other.celdas[1][1])
        s3 = (self.celdas[1][0])*(other.celdas[0][0]) + (self.celdas[1][1])*(other.celdas[1][0])
        s4 = (self.celdas[1][0])*(other.celdas[0][1]) + (self.celdas[1][1])*(other.celdas[1][1])
        f1.append(s1)
        f1.append(s2)
        f2.append(s3)
        f2.append(s4)
        m.append(f1)
        m.append(f2)
        self.celdas = m
        return Matriz(m)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
