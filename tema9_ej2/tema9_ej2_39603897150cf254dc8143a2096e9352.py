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
      self.other=other
      a=self.celdas[0][0]*self.other[0][0] + self.celdas[0][1]*self.other[1][0]
      b=self.celdas[0][0]*self.other[0][1] + self.celdas[0][1]*self.other[1][1]
      c=self.celdas[1][0]*self.other[0][0] + self.celdas[1][1]*self.other[1][0]
      d=self.celdas[1][0]*self.other[0][1] + self.celdas[1][1]*self.other[1][1]
          
      
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           