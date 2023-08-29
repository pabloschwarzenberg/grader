class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        if len(self.celdas)==len(other.celdas[0])  and len(other.celdas)==len(self.celdas[0]):
           
            matriz1=[]
            a=[]
            
            #debe tener tamaño de nº filas de la primera
            for i in range(len(self.celdas)):
               for x in range(len(self.celdas)):
                  a.append(0)
               matriz1.append(a)
               a=[]
            
            #for para filas
            k1=0
            k2=0
            for i in range(len(self.celdas)):
              for x in range(len(self.celdas)):
                resultado=0
                for z in range(len(other.celdas)):
                  a= self.celdas[k1][z]*other.celdas[z][k2]
                  print(self.celdas[k1][z])
                  resultado+=a
                k2+=1
                matriz1[i].pop(x)
                matriz1[i].insert(x,resultado)
              k1+=1
              k2=0
            matriz_final=Matriz(matriz1)
            return matriz_final
            
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
