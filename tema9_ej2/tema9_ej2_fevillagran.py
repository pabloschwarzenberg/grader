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

    def __mul__(self, matriz1, matriz2):
        self.matriz1 = matriz1
        self.matriz2 = matriz2
        matrizf = []
        for i in range(0,len(self.matriz1)):
            for j in range(0,len(self.matriz1)):
                for k in range(0,len(self.matriz1)):
                    matrizf[i][j]+= self.matriz1[i][k] * self.matriz2[k][j]
        return matrizf

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           