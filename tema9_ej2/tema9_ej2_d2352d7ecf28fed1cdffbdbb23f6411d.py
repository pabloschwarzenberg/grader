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
        resultado=[]
        a=int(self.celdas[0][0])
        b=int(self.celdas[0][1])
        c=int(self.celdas[1][0])
        d=int(self.celdas[1][1])

        x=int(other.celdas[0][0])
        y=int(other.celdas[0][1])
        z=int(other.celdas[1][0])
        w=int(other.celdas[1][1])

        a1=a*x + b*z
        a2=a*y + b*w
        b1=c*x + d*z
        b2=c*y + d*w
        self.celdas=[[a1,a2],[b1,b2]]
        
        return self


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           