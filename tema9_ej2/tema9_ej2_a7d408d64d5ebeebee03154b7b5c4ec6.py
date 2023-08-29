import math
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
        i=0
        fin=[]
        while i<len(self.celdas):
            k=0
            while k<len(self.celdas):
                for l in range(len(other.celdas[0])):
                    d=int(self.celdas[i][1])*int(other.celdas[1][k])
                    fin.append(d)
                k+=1
            i+=1
            k-=len(self.celdas)
        
        c=Matriz(fin)
        return c

if __name__ == "__mainin__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)