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

    def __mul__(self, b):
        mr=[]
        fila1=[]
        fila2=[]
        n1=self.celdas[0][0]*b.celdas[0][0]+self.celdas[0][1]*b.celdas[1][0]
        n2=self.celdas[0][0]*b.celdas[0][1]+self.celdas[0][1]*b.celdas[1][1]
        n3=self.celdas[1][0]*b.celdas[0][0]+self.celdas[1][1]*b.celdas[1][0]
        n4=self.celdas[1][0]*b.celdas[0][1]+self.celdas[1][1]*b.celdas[1][1]
        fila1.append(n1)
        fila1.append(n2)
        fila2.append(n3)
        fila2.append(n4)
        mr=[fila1,fila2]    
        return mr

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
    c=Matriz(r)
    print(c)
           