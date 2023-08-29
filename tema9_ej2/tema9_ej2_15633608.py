def multi_matriz(m1,m2):
    mr=[]
    i=0
    j=0
    d1= len(m1[1])
    d2= len(m2)
    d3=len(m1)
    d4=len(m2[1])
    if d1 != d2:
        print("Las matrices no se pueden multiplicar")
        return mr
    for e in range(0,d3):
        fila=[]
        for o in range(0,d4):
            suma=0
            for i in range(0,d1):
                suma=suma+m1[e][i]*m2[i][o]
            fila.append(suma)
        mr.append(fila)
    return mr

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
        a=self.celdas
        b=other.celdas
        return Matriz(multi_matriz(a,b))

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           
         