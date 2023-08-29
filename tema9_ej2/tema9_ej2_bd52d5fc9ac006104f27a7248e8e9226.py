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
        m = int(len(self.celdas))
        n = int(len(self.celdas[0]))
        p = int(len(other.celdas[0]))
        c = []
        for i in range(m):
          fila=[]
          for j in range(n):
            sum=0
            for k in range(0, p):
              sum+=self.celdas[i][k] * other.celdas[k][j]
            fila.append(sum)
          c.append(fila)
        d = Matriz(c)
        print(c)
        return d

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
   