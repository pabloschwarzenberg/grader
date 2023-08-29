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
        a=self.celdas[0][0]
        b=self.celdas[0][1]
        c=self.celdas[1][0]
        d=self.celdas[1][1]
        e=other.celdas[0][0]
        f=other.celdas[0][1]
        g=other.celdas[1][0]
        h=other.celdas[1][1]
        multiplicacion=[[a*e+c*f,e*b+d*f],[a*g+c*h,b*g+d*h]]
        return multiplicacion
      
        

if __name__ == "__main__":
  pass
           