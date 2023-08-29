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
        res = []
        
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(self.celdas[0])):
                suma = 0
                for k in range(len(other.celdas)):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                row.append(suma)
            res.append(row)
        
        return Matriz(res)