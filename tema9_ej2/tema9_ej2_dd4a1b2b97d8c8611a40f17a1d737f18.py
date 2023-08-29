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
        men=[]
        women=[]
        for i in self.celdas:
            for j in i:
                men.append(j)
        for k in other.celdas:
            for i in k:
                women.append(i)
        a=men[0]*women[0]+men[1]*women[2]
        b=men[0]*women[1]+men[1]*women[3]
        c=men[2]*women[0]+men[3]*women[2]
        d=men[2]*women[1]+men[3]*women[3]
        return Matriz([[a,b],[c,d]])

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           