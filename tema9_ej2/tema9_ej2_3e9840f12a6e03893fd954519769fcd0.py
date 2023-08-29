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
        resultado1=[]
        resultado2=[]
        sum=0
        sum1=0
        sum2=0
        sum3=0
        for x in range(2):
            sum += other.celdas[x][0] * self.celdas[1][x]
            sum1 += other.celdas[x][1] * self.celdas[1][x]
            sum2 += other.celdas[x][0] * self.celdas[0][x]
            sum3 += other.celdas[x][1] * self.celdas[0][x]
        resultado1.append(sum)
        resultado1.append(sum1)
        resultado2.append(sum2)
        resultado2.append(sum3)
        return Matriz([resultado2,resultado1])