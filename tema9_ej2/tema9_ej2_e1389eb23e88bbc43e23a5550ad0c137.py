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
    
    def multiplicar(self, fila, columna):
        
        resultado = 0
        for i in range(len(fila)):
            resultado += fila[i] * columna[i]
        return resultado
    
    def obtener_columna(self, matriz, index):
        
        columna = []
        
        for i in matriz:
            columna.append(i[index])
        return columna

    def __mul__(self, other):
        
        n_col = len(self.celdas)
        n_fila = len(self.celdas[0])
        
        nueva_col = []
        nueva_fil = []
        
        for j in range(n_col):
            for i in range(n_fila):
                nueva_fil.append(0)
            nueva_col.append(nueva_fil)
            nueva_fil = []
        
        for i in range(len(nueva_col)):
            for j in range(len(nueva_col[0])):
                
                col = self.obtener_columna(other.celdas, j)
                fila = self.celdas[i]
                mul = self.multiplicar(fila, col)
                nueva_col[i][j] = mul
 
        print(Matriz(nueva_col))
        
        
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           