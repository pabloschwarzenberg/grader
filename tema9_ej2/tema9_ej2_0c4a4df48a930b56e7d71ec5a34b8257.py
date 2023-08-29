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
        s=[]
        for i in self.celdas:
          m=0
          suma1=0
          h=0
          for j in i:
                suma1+=j*other.celdas[m][h]
                m+=1
          m=0
          h=1
          suma2=0
          for j in i:
                suma2+=j*other.celdas[m][h]
                m+=1
          s.append([suma1,suma2])
    
        return Matriz(s)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)

