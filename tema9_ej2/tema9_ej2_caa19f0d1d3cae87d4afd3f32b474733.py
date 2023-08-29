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
      if len(self.celdas) == 0 or len(other.celdas) == 0:
        return Matriz()
        
      rows_self = len(self.celdas)
      cols_self = len(self.celdas[0])
      rows_other = len(other.celdas)
      cols_other = len(other.celdas[0])
      
      if cols_self != rows_other:
        raise ValueError("Cannot multiply matrices. Invalid dimensions")
      result = [[0 for _ in range(cols_other)] for _ in range(rows_self)]
      
      for i in range(rows_self):
        for j in range(cols_other):
          for k in range(cols_self):
            result[i][j] += self.celdas[i][k]*other.celdas[k][j]
      return Matriz(result)
            

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           