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
        p=[]
        f=[]
        t=[]
        for i in list(range(len(self.celdas))):
            t=[]
            for j in list(range(len(self.celdas[i]))):
                r=0
                for k in list(range(len(other.celdas[0]))):
                    r+=self.celdas[i][k]*other.celdas[k][j]
                t.append(r)
            f.append(t)
            p.append(f)
        return Matriz([p])
            
       

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           