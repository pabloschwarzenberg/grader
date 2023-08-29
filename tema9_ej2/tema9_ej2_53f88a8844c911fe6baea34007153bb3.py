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
        r=[[],[]]
        for i in range(len(self.celdas)):
            n=0
            o=0
            for j in range(len(other.celdas)):
                #i=0 and j=0 --> [0][0]*[0][0] --> j=1 --> [0][1]*[1][0]
                #i=1 and j=0 --> [1][0]*[0][0] --> j=1 --> [1][1]*[1][0] 
                n+=self.celdas[i][j]*other.celdas[j][0]
                o+=self.celdas[i][j]*other.celdas[j][1]
            r[i].append(n)
            r[i].append(o)
        return Matriz(r)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)