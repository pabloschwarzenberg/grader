class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas
        self.tamaño=len(celdas)
        
    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        final=[]
        tamaño=self.tamaño
        for i in range(tamaño):
            parcial=[]
            for z in range(tamaño):
                suma=0
                for w in range(tamaño):
                    suma+=self.celdas[i][w]*other.celdas[w][z]
                parcial.append(suma)
            final.append(parcial)
        return(final)        

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           