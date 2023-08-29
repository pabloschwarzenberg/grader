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

    def __mul__(a, b):
      if len(a[0])==len(b):
        m3=[]
        for i in range(len(a)):
          m3.append([])
          for j in range(len(b[0])):
            m3[i].append(0)
            
        for i in range(len(a)):
          for j in range(len(b[0])):
            for k in range(len(a[0])):
              m3[i][j] += a[i][k] * b[k][j]
        return m3
        
      

           