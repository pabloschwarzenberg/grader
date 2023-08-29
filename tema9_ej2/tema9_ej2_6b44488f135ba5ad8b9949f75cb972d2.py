class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        d=len(self.celdas)
        mr=[]
        for l in range(d):
          mr.append([0]*d)
        for i in range(d):
          for j in range(d):
            for k in range(d):
              mr[i][j]+= (self.celdas[i][k])*(other.celdas[k][j])
        MR=Matriz(mr)
        return MR

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           