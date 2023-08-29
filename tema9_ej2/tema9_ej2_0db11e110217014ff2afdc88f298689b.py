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

        def __mul__(self,other):
          matriz=[]
          fila1=[]
          fila2=[]
          a=self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0]
          b=self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]
          fila1.append(a)
          fila1.append(b)
          c=self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0]
          d=self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]
          fila2.append(c)
          fila2.append(d)
          matriz.append(fila1)
          matriz.append(fila2)
          return matriz

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
           