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
        multiplicacion = []
        print(len(self.celdas), len(self.celdas[0]))
        for i in range(len(self.celdas)):
            x = 0
            multiplicacion.append([])
            for rango in range(len(self.celdas)):
                h = 0
                multiplicar = 0
                for j in self.celdas[i]:
                    m = other.celdas[h][x]
                    print(len(other.celdas[x]))
                    print(j, "*", m)
                    multiplicar += j * m
                    print(multiplicar)
                    h += 1
                x += 1
                multiplicacion[i].append(multiplicar)
        multiplicacion = Matriz(multiplicacion)
        return multiplicacion

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           