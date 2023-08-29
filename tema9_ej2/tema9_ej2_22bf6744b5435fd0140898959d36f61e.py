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
        lista=[]
        pre_lista=[]
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                x=self.celdas[i][j]*other.celdas[i][j]
                pre_lista.append(x)
            lista.append(pre_lista)
            pre_lista=[]
        return lista

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           