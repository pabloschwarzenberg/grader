class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
            s=s.split('\n')
        return s

    def __mul__(self, other):
        mult=[[0,0],[0,0]]
        for i in range(0,2):
            for j in range(0,2):
                for k in range(0,2):
                    mult[i][j]=self.celdas[i][k]*other.celdas[k][j]
        return mult
                
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
