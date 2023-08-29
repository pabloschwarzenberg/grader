#multiplicacion matrices:
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
    def __mul__(self,other):
        r=Matriz()
        i=0
        fila=[]
        a=self.celdas
        dato1=self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0]
        dato2=self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1]
        fila.append(dato1)
        fila.append(dato2)
        r.celdas.append(fila)
        fila=[]
        dato3=self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0]
        dato4=self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1]
        fila.append(dato3)
        fila.append(dato4)
        r.celdas.append(fila)
        return  r
                
       

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)