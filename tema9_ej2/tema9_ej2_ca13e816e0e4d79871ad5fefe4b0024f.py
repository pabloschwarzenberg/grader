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
        suma=0
        suma1=0
        suma2=0
        suma3=0
        res=[]
        res1=[]
        for i in range(2):
            suma+= other.celdas[i][0]*self.celdas[1][i]
            suma1+=other.celdas[i][1]*self.celdas[1][i]
            suma2+=other.celdas[i][0]*self.celdas[0][i]
            suma3+=other.celdas[i][1]*self.celdas[0][i]
        res.append(suma)
        res.append(suma1)
        res1.append(suma2)
        res1.append(suma3)
        sol= Matriz([res1,res])
        return sol
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           