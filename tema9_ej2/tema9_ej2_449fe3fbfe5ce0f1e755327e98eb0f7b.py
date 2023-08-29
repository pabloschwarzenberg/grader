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
        resultado=[]
        c=0
        while c<len(self.celdas):
            resultado.append([])
            for lugar in range(len(self.celdas)):
                resultado[c].append(0)
            c=c+1
        i=0
        while i<len(self.celdas):
            j=0
            while j<len(self.celdas):
                k=0
                operacion=[]
                while k<len(self.celdas):
                    entrada = self.celdas[i][k]*other.celdas[k][j]
                    operacion.append(entrada)
                    k = k+1
                suma=0
                for nro in operacion:
                    suma = suma+nro
                resultado[i][j]=suma
                j=j+1
            i=i+1
        resultado=Matriz(resultado)
        return resultado

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           