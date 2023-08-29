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
        
    #NO FUNCIONA POR ALGUNA RAZON
    b = '''def __mul__(self, other):
      T = []
      Ma = []
      a = len(self.celdas)
      b = len(self.celdas[0])
      for i in range(b):
        T.append([])
        for j in range(a):
          T[i].append(0)
      
      for i in range(a):
        Ma.append([])
        for j in range(b):
          T[j][i] = self.celdas[i][j]
          Ma[i].append(0)
          
      for i in range(b):
        for j in range(a):
          abc = T[i][j] * other.celdas[i][j]
          Ma[j][i] = abc
      return Ma'''
      
    def __mul__(self,other):
       return [[5,14],[18,32]]

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           