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
        n=0
        lista1=[]
        while n<2:
            m=0
            q=0
            while m<2:
                a=int(self.celdas[n][q])*int(other.celdas[q][m])
                b=int(self.celdas[n][q+1])*int(other.celdas[q+1][m])
                
                m=m+1
                d=a+b
                d=str(d)+' '
                lista1.append(d)
            return lista1
            n=n+1

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           