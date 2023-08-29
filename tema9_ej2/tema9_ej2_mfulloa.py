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
        if len(self.celdas[0])==len(other.celdas):
            matriz=[[0,0],[0,0]]
            for w in range(len(other.celdas)):
                for j in range(len(self.celdas[0])):
                    for i in range(len(self.celdas)):
                        matriz[j][w]+=self.celdas[j][i]*other.celdas[i][w]
            a=Matriz(matriz)
            return a
        return False

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
