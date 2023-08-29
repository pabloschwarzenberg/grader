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

    def __mul__(self,matriz1,matriz2):
      matriz1=Matriz([a,b],[c,d])
      matriz2=Matriz([e,f],[g,h])
      resultadomatriz=Matriz([a*e+c*f,b*e+d*f],[a*g+c*h,b*g+d*h])
      return resultadomatriz

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=__mul__(a,b)
    r=a*b
    print(r)
           