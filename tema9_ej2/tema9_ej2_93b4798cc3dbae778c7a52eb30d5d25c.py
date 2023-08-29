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
        c=0
        d=0
        r=0
        m1=self.celdas
        m2=other.celdas
        mr=[[] for _ in range(len(m1))]

        
        while c<len(m1):
            for i in range(len(m1)):
                r=r+m1[c][i]*m2[i][d]
        
            mr[c].append(r)
            d+=1
            r=0
            if d==len(m1):
                c+=1
                d=0
                continue
        return Matriz(mr)
        

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           