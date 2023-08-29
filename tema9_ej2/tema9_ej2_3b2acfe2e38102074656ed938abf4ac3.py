class Matriz:
    def __mul__(self,other):
      m=[]
      for i in range(len(self.celdas)):
        for j in range(len(self.celdas)):
          m.append(self.celdas[i][0]*other.celdas[0][j] + self.celdas[i][1]*other.celdas[1][j])
          r = [[m[0], m[1]],[m[2], m[3]]]
      return Matriz(r)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           