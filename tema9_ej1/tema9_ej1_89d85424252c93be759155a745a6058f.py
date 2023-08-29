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
        a = (self[0][0] * other[0][0]) + (self[0][1] * other[0][0])
        b = (self[0][0] * other[0][1]) + (self[0][1] * other[1][0])
        c = (self[1][0] * other[0][0]) + (self[1][1] * other[0][1])
        d = (self[1][0] * other[0][1]) + (self[1][1] * other[1][1])

        return [[a,b],[c,d]]