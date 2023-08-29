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
      if len(self.celdas[0]) != len(other.celdas):
        raise ValueError("Las matrices no se pueden multiplicar")
      filas = len(self.celdas)
      columnas = len(other.celdas[0])
      celdas = [[0 for j in range(columnas)] for i in range(filas)]
      resultante = Matriz(celdas)
    
      for i in range(filas):
        for j in range(columnas):
            producto = 0
            for k in range(len(self.celdas[0])):
                producto += self.celdas[i][k] * other.celdas[k][j]
            resultante.celdas[i][j] = producto
            
      return resultante

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           