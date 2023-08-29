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
        lista = []
        i = 0
        j = 0
        for vector in self.celdas:
          if j< len(self.celda)
            for numero in vector:
              if i< len(self.celda)
               valor = self.celda[i][j]*self.other[i][j] + self.celda[i][j+1]*self.other[i][j+1]
               lista.append(valor)
               i = i + 1 
               j = j + 1
         return lista 
               
               
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           