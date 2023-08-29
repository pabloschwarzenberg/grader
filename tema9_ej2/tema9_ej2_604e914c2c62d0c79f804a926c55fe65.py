class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas
        self.f1=celdas[0]
        self.f2=celdas[1]

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s
    
    
    def __mul__(self,other):
        r1=(self.f1[0]*other.f1[0])+(self.f1[1]*other.f2[0])
        r2=(other.f1[1]*self.f1[0])+(self.f1[1]*other.f2[1])
        r3=(self.f2[0]*other.f1[0])+(self.f2[1]*other.f2[0])
        r4=(other.f1[1]*self.f2[0])+(self.f2[1]*other.f2[1])
        m=[[r1,r2],[r3,r4]]
        return Matriz (m)
        
if __name__ == "__main__":
    
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)