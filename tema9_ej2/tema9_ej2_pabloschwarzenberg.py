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
        matriz_mul=[]
        for i in range(len(self.celdas)):
#No estabas entregando una matriz (que es una lista de listas, sino que una lista con todas las celdas de la matriz)
            fila=[]
            for k in range(len(self.celdas)):
                x = 0
                for j in range(len(self.celdas)):
                    x += self.celdas[i][j]*other.celdas[j][k]
                #debes ir construyendo cada fila elemento a elemento
                fila.append(x)
            #cuando terminas de calcular la fila, la agregas a la matriz de resultado
            matriz_mul.append(fila)
#el método __mul__ debe retornar un objeto de la clase Matriz
        return Matriz(matriz_mul)

#para que openedx pueda revisar tu programa, la parte principal debe estar dentro de este IF
if __name__ == "__main__":
    ejemplo1=Matriz([[1,2],[3,4]])
    ejemplo2=Matriz([[5,6],[7,8]])
    m=ejemplo1*ejemplo2
    print(m)
