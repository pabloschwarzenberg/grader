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
        a=int(repr(self)[4])*int(repr(other)[4])+int(repr(self)[10])*int(repr(other)[17])
        b=int(repr(self)[4])*int(repr(other)[10])+int(repr(self)[10])*int(repr(other)[23])     
        c=int(repr(self)[17])*int(repr(other)[4])+int(repr(self)[23])*int(repr(other)[17])
        d=int(repr(self)[17])*int(repr(other)[10])+int(repr(self)[23])*int(repr(other)[23])
        r=Matriz([[a,b],[c,d]])
        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           