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
      return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*other.celdas)] for X_row in self.celdas]
a=Matriz([[1,2],[3,4]])
b=Matriz([[5,6],[7,8]])
r=a*b
print(r)
           