class Matriz:
    def __init__(self,matriz,celdas=[]):
        self.celdas=celdas
        self.matriz=matriz

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        matriz1=self.celdas
        matriz2=other.celdas
        otra_matriz=[]
        nueva_matriz=[]
        for i in range(len(matriz2)):
            columna=[]
            for j in range(len(matriz2)):
                a=matriz2[j][i]
                columna.append(a)
            otra_matriz.append(columna)
        for i in range(len(matriz1)):
            columna=[]
            for j in range(len(matriz1)):
                a=matriz1[i][j]*otra_matriz[i][j]
                b=matriz1[i][j+1]*otra_matriz[i][j+1]
                c=a+b
                d=columna.append(c)
            nueva_matriz.append(d)
        return nueva_matriz

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           