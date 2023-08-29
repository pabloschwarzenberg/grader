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
        s0=0
        s1=0
        s2=0
        s3=0
        r0=[]
        r1=[]
        for i in range(2):
            s0+= other.celdas[i][0]*self.celdas[1][i]
            s1+=other.celdas[i][1]*self.celdas[1][i]
            s2+=other.celdas[i][0]*self.celdas[0][i]
            s3+=other.celdas[i][1]*self.celdas[0][i]
        r0.append(s0)
        r0.append(s1)
        r1.append(s2)
        r1.append(s3)
        sol= Matriz([r1,r0])
        return sol
if __name__ == "__main__":
    m1=Matriz([[1,2],[3,4]])
    m2=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)           