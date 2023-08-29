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
        i=0
        r=[]
        while i<len(self.celdas):
            k=0
            d=[]
            while k<len(self.celdas):
                c=0
                for j in range(0,len(self.celdas)):
                    c=c+self.celdas[i][j]*other.celdas[j][k]
                d.append(c)
                k=k+1
            r.append(d)
            i=i+1
        return Matriz(r)
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           