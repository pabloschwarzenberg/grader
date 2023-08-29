class Matriz:
    def __init__(self,celdas):
        self.fil=celdas[0]
        self.fil2=celdas[1]
        self.celdas=celdas
    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s
    def __mul__(self,b):
        A=self.fil[0]
        B=self.fil[1]
        E=b.fil[0]
        F=b.fil[1]
        C=self.fil2[0]
        D=self.fil2[1]
        G=b.fil2[0]
        H=b.fil2[1]
        I=(A*E)+(B*G)
        K=(C*E)+(D*G)
        J=(F*A)+(B*H)
        L=(F*C)+(D*H)
        MA=[[I,J],[K,L]]
        return Matriz(MA)     


if __name__ == "__main__":
    
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    R=a.__mul__(b)
    print(R)
           

           