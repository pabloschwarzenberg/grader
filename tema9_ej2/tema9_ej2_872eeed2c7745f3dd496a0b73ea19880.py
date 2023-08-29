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

        if(len(self.celdas)!=len(other.celdas)):
            return None

        mat=[]


        for i in range(len(self.celdas)):

            fila=[]
            
            for r in range(len(self.celdas)):
                celda=0
                
                for j in range(len(self.celdas)):

                    print(self.celdas[i][j],other.celdas[j][r])

                    celda=celda+(self.celdas[i][j]*other.celdas[j][r])

                    print(celda)

                fila.append(celda)

            mat.append(fila)

        resultado=Matriz(mat)


                

        return resultado

        pass

    def __add__(self,other):
        r=[]
        if(len(self.celdas)!=len(other.celdas)):
            return None
        for i in range(len(self.celdas)):
            fila=[]
            for j in range(len(self.celdas)):
                c=self.celdas[i][j]+other.celdas[i][j]
                fila.append(c)
            r.append(fila)
        resultado=Matriz(r)
        return resultado

    

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           