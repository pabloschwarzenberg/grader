class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        m=""
        for a in range(len(self.celdas)):
            for b in range(len(self.celdas)):
                m+="{0: >5} ".format(self.celdas[a][b])
            m+="\n"
        return m

    def __mul__(self, other):
        suma=0
        suma1=0
        suma2=0
        suma3=0
        res2=[]
        res1=[]
        for a in range(2):
            suma+= other.celdas[a][0]*self.celdas[1][a]
            suma1+=other.celdas[a][1]*self.celdas[1][a]
            suma2+=other.celdas[a][0]*self.celdas[0][a]
            suma3+=other.celdas[a][1]*self.celdas[0][a]
        res2.append(suma)
        res2.append(suma1)
        res1.append(suma2)
        res1.append(suma3)
        sol= Matriz([res1,res2])
        return sol
if __name__ == "__main__":
    x=Matriz([[1,2],[3,4]])
    y=Matriz([[5,6],[7,8]])
    z=x*y
    print(z)