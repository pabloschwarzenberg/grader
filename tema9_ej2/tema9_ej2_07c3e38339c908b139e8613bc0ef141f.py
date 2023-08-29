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

    def __mul__(self,other):
        mr= []
        f=0
        d1=len(self.celdas)       
        while f<d1:
          filamr=[]
          mfc=((self.celdas[f][0]*other.celdas[0][0])+(self.celdas[f][1]*other.celdas[1][0]))
          mfc2=((self.celdas[f][0]*other.celdas[0][1])+(self.celdas[f][1]*other.celdas[1][1]))
          filamr.append(mfc)
          filamr.append(mfc2)
          mr.append(filamr)
          f=f+1
        mrr= Matriz(mr)
        return mrr
        

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           