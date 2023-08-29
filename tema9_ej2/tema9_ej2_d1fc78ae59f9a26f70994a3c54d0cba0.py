class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas
        
    def __mul__(self, other):
        c=Matriz()
        c.celdas[0][0]=self.celdas[0][0]*other[0][0]+self.celdas[0][1]*other[1][0]
        c.celdas[0][1]=self.celdas[0][0]*other[0][1]+self.celdas[0][1]*other[1][1]
        c.celdas[1][0]=self.celdas[1][0]*other[0][0]+self.celdas[1][1]*other[1][0]
        c.celdas[1][1]=self.celdas[1][0]*other[0][1]+self.celdas[1][1]*other[1][1]
        return c

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           