def __mul__(self, other):
          m = Matriz([])
          m=Matriz([[self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0],
             self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]],
             [self.celdas[1][0]*other.celdas[0][0]+self