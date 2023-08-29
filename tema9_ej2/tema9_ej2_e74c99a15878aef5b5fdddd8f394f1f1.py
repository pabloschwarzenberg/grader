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
        d1=len(self.celdas)
        i=0
        while i<d1:
            filai=[]
            j=0
            while j<d1:
                mij=0
                k=0
                while k<d1:
                    mij=mij+self.celdas[i][k]*other.celdas[k][j]
                    k=k+1
                filai.append(mij)
                j=j+1
            mr.append(filai)
            i=i+1
        return Matriz(mr)