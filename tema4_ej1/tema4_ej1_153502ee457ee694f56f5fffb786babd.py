class Matriz:
    def init(self,celdas=[]):
        self.celdas=celdas

    def repr(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def mul(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]other.celdas[0][0]+self.celdas[0][1]other.celdas[1][0],
             self.celdas[0][0]other.celdas[0][1]+self.celdas[0][1]other.celdas[1][1]],
             [self.celdas[1][0]other.celdas[0][0]+self.celdas[1][1]other.celdas[1][0],
             self.celdas[1][0]other.celdas[0][1]+self.celdas[1][1]other.celdas[1][1]]])
          return m
if name == "main":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    print(a,b)
    r=a*b
    print(r)
         