class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas
    def multiplicar(self,matriz2):
        matriz_nueva=[]
        f11=self.celdas[0][0]*matriz2.celdas[0][0]+self.celdas[0][1]*matriz2.celdas[1][0]
        f12=self.celdas[0][0]*matriz2.celdas[0][1]+self.celdas[0][1]*matriz2.celdas[1][1]
        matriz_nueva.append([f11,f12])
        f21=self.celdas[1][0]*matriz2.celdas[0][0]+self.celdas[1][1]*matriz2.celdas[1][0]
        f22=self.celdas[1][0]*matriz2.celdas[0][1]+self.celdas[1][1]*matriz2.celdas[1][1]
        matriz_nueva.append([f21,f22])
        print(matriz_nueva)
    
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    
    a.multiplicar(b)
           