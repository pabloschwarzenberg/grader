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
        if len(self.celdas)!=len(other.celdas):
            return None
        lista1=[]
        lista2=[]
        i=0
        j=0
        while i<len(other.celdas) and j<len(other.celdas):
            lista1.append(other.celdas[i][j])
            i=i+1
            if i==len(other.celdas):
                lista2.append(lista1)
                lista1=[]
                j=j+1
                i=0
        fila_mul=[]
        r=[]
        
        fila1=0
        fila2=0
        elem1=0
        elem2=0
        a=0
        while elem1<len(self.celdas) and elem2<len(lista2):
            a=a+(self.celdas[fila1][elem1]*lista2[fila2][elem2])
            elem1=elem1+1
            elem2=elem2+1
            if elem1==len(self.celdas) and elem2==len(lista2):
                fila_mul.append(a)
                elem1=0
                elem2=0
                a=0
                fila2=fila2+1
                if fila2==len(lista2):
                    r.append(fila_mul)
                    fila_mul=[]
                    fila2=0
                    fila1=fila1+1
                    if fila1==len(self.celdas):
                        break
        
        return Matriz(r)
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
