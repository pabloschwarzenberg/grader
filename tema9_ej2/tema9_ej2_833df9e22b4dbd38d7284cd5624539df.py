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
      for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
            lista=[]
            a=self.celdas[i][j]*other[i][j]
            b=self.celdad[i][j+1]*other[i+1][j]
            c=a+b
            lista.append(c)
      matriz.append(lista)
      return(matriz)
        return 

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           