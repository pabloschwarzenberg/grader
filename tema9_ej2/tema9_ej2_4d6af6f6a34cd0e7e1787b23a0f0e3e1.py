class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas
        self.fila1=celdas[0]
        self.fila2=celdas[1]

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s
    
    
    def __mul__(self,matriz2):
        r1=(self.fila1[0]*matriz2.fila1[0])+(self.fila1[1]*matriz2.fila2[0])
        r2=(matriz2.fila1[1]*self.fila1[0])+(self.fila1[1]*matriz2.fila2[1])
        r3=(self.fila2[0]*matriz2.fila1[0])+(self.fila2[1]*matriz2.fila2[0])
        r4=(matriz2.fila1[1]*self.fila2[0])+(self.fila2[1]*matriz2.fila2[1])
        Aresultante=[[r1,r2],[r3,r4]]
        return Matriz (Aresultante)
        
if __name__ == "__main__":
    
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    R=a.__mul__(b)
    print(R)
           