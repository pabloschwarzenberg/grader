def matriz_ceros(m, n):
      aux = []
      for i in range(m):
        aux.append([0]*n)
      return Matriz(aux)

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
      output = matriz_ceros(len(self.celdas), len(other.celdas[0]))
      for i in range(len(self.celdas)):
        for j in range(len(other.celdas[0])):
          for k in range(len(self.celdas[0])): 
            output.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]      
      return output
            
               

if __name__ == "__main__":
  a=Matriz([[1,2],[3,4]])
  b=Matriz([[5,6],[7,8]])
  r=a*b
  print(r)
           