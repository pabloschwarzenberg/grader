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
        a = int(self.celdas[0][0])
        b = int(self.celdas[0][1])
        c = int(self.celdas[1][0])
        d = int(self.celdas[1][1])
        e = int(other.celdas[0][0])
        f = int(other.celdas[0][1])
        g = int(other.celdas[1][0])
        h = int(other.celdas[1][1])
        A = a*e + b*g
        B = a*f + b*h
        C = c*e + d*g
        D = c*f + d*h
        self.celdas=([[A,B],[C,D]])
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           