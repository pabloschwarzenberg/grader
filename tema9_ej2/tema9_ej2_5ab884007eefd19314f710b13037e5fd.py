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
      matriz=[]
      for i in range(0,len(self.celdas)):
        fila=[]
        for j in range(0,len(self.celdas)):
            a=0
            for k in range(0,len(other.celdas)):
                a=a+self.celdas[i][k]*other.celdas[k][j]
            fila.append(a)
        matriz.append(fila)
      matriz=Matriz(matriz)
      return matriz

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           