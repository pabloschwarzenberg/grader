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
        matriz=[]
        fil=[]
        fil1=[]
        a=self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0]
        b=self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]
        fil.append(a)
        fil.append(b)
        c=self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0]
        d=self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]
        fil1.append(c)
        fil1.append(d)
        matriz.append(fil)
        matriz.append(fil1)
        return Matriz(matriz)
         
 
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           