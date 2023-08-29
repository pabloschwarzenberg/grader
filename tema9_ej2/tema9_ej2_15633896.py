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

        filai=[]
        matriz=[]
        suma=0

        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                    for y in range(len(self.celdas)):
                        multi=self.celdas[i][y]*other.celdas[y][j]
                        suma=suma+multi
                    filai.append(suma)
                    suma=0

            matriz.append(filai)
            filai=[]


        return matriz

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)