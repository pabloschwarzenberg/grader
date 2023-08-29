class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        f=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                f+="{0: >5} ".format(self.celdas[i][j])
            f+="\n"
        return f

    def __mul__(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0],
             self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]],
             [self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0],
             self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]]])
          return m


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r= a*b
    print(r)
           