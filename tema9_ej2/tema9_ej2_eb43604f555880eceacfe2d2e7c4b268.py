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
        nuevo=Matriz([[],[]])
        nuevo.celdas[0].append(self.celdas[0][0]*other.celdas[0][0]+self.celdas[0][1]*other.celdas[1][0])
        nuevo.celdas[0].append(self.celdas[0][0]*other.celdas[0][1]+self.celdas[0][1]*other.celdas[1][1])
        nuevo.celdas[1].append(self.celdas[1][0]*other.celdas[0][0]+self.celdas[1][1]*other.celdas[1][0])
        nuevo.celdas[1].append(self.celdas[1][0]*other.celdas[0][1]+self.celdas[1][1]*other.celdas[1][1])
        return nuevo

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           