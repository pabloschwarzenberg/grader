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
        mr=[]
        i=0
        j=0
        k=0
        m1=self.celdas
        m2=other.celdas
        d1=len(m1)
        d2=len(m2)
        if d1!=d2:
            print("Las matrices no se pueden sumar porque no tienen la misma dimension")
            return mr
        while i<d1:
            filai=[]
            while j<d1:
                mij=0
                while k<d1:
                    mij=mij+m1[i][k]*m2[k][j]
                    k=k+1
                filai.append(mij)
                j=j+1
                k=0
            mr.append(filai)
            i=i+1
            j=0
        return Matriz(mr)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           