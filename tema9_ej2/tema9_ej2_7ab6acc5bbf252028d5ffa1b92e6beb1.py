class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas
        self.A =[]
        i=0
        while i < len(self.celdas):
            self.A.append([])
            j = 0
            while j < len(self.celdas[0]):
                self.A[i].append([])
                j += 1
            i += 1

    def __repr__(self):
        A = ""
        i=0
        while i<len(self.celdas):
            j=0
            while j<len(self.celdas[0]):
                A=A+str(self.celdas[i][j])+" "
                j+=1
            A = A + "\n"
            i+=1

        return A
    
    def __mul__(self,other):
        if len(self.celdas[0])==len(other.celdas):
            i=0
            while i<len(self.celdas):
                j=0
                while j<len(other.celdas[0]):
                    contador=0
                    k=0
                    while k<len(self.celdas):
                        contador=contador+self.celdas[i][k]*other.celdas[k][j]
                        k+=1
                    self.A[i][j]=contador
                    j+=1
                i+=1
            return self.A
        else:
            return "el numero de columnas de la primera matriz debe ser igual al numero de filas de la primera matriz"

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           