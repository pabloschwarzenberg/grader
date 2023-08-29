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
        celdas = []
        i = 0
        while i < len(self.celdas[0]):
            fila = []
            a = 0
            j = 0
            while j < len(self.celdas[0]):
                a +=  self.celdas[i][j] * other.celdas[j][i]
                j += 1
            celdas.append(fila)
            i += 1
        self.celdas = celdas    
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           