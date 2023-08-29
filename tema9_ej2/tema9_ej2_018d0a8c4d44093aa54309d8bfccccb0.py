class Matriz:
    def __init__(self,celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        l = []
        la = []
        for w in range (0,len(self.celdas)):
            for x in range(0,len(other.celdas)):
                i = 0
                for z in range(len(self.celdas)):
                    i = i + (self.celdas[w][x] * other.celdas[z][x])
                la = la + [i]
            l = l + la
            la = []
        lb= Matriz(l)
        return lb

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           