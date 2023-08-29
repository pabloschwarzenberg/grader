class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        L=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                L+="{0: >5} ".format(self.celdas[i][j])
            L+="\n"
        return L

    def __mul__(self, other):
        L2=[]
        L3=[]
        sum=0
        sum1=0
        sum2=0
        sum3=0
        for x in range(2):
            sum += other.celdas[x][0] * self.celdas[1][x]
            sum1 += other.celdas[x][1] * self.celdas[1][x]
            sum2 += other.celdas[x][0] * self.celdas[0][x]
            sum3 += other.celdas[x][1] * self.celdas[0][x]
        L2.append(sum)
        L2.append(sum1)
        L3.append(sum2)
        L3.append(sum3)
        return Matriz([L3,L2])
           

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           