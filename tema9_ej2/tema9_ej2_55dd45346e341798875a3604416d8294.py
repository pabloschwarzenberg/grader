class Matriz:
    def __init__(self,celdas = []):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
      resultado = []
      for fila in range(len(self.celdas)):
        sub = []
        for columna in range(len(other.celdas)):
          suma = 0
          for i in range(len(self.celdas)):
            aux = self.celdas[fila][i] * other.celdas[i][columna]
            suma += aux
          sub.append(suma)
        resultado.append(sub)
      return Matriz(resultado)
        

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           