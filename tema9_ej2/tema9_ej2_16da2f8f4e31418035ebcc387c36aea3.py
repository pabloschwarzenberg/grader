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
        r=Matriz()
        i=0
        while i<len(self.celdas):
            j=0
            fila_r=[]
            while j<len(self.celdas[i]):
                s=self.celdas[i][0]*b.celdas[0][j]+self.celdas[i][1]*b.celdas[1][j]
                fila_r.append(s)               
                j+=1
            r.celdas.append(fila_r)
            i+=1
        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           