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
        sumaA=0
        sumaB=0
        sumaC=0
        resta=[]
        resta1=[]
        for i in range(2):
            suma+= other.celdas[i][0]*self.celdas[1][i]
            sumaA+=other.celdas[i][1]*self.celdas[1][i]
            sumaB+=other.celdas[i][0]*self.celdas[0][i]
            sumaC+=other.celdas[i][1]*self.celdas[0][i]
        resta.append(suma)
        resta.append(suma1)
        resta1.append(suma2)
        resta1.append(suma3)
        sol= Matriz([resta1,resta])
        return sol
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
