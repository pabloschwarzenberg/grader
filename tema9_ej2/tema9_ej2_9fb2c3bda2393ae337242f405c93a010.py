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
        r=Matriz()
        i=0
        d=len(self.celdas)
        cfila=[]
        while i<d:
          j=0
          fila=[]
          while j<d:
            ef=0
            k=0
            while k<d:
              ef=ef+self.celdas[i][k]*other.celdas[k][j]
              k=k+1
            fila.append(ef)
            j=j+1
          cfila.append(fila)
          i=i+1
        r.celdas=cfila
        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           