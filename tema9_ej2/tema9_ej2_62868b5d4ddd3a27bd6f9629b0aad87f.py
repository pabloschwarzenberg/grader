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
        matriz=[]
        a=[]
        a1=0
        for i in range(2):
            if i==1:
                a.append(a1)
            for j in range(2):
                s=self.celdas[i][j]
                s1=other.celdas[j][i]
                en=int(s)*int(s1)
                a1+=en
        a1=0
        for i in range(2):
            if i == 1:
                a.append(a1)
            for j in range(2):
                    s = self.celdas[1][j]
                    s1 = other.celdas[j][i]
                    en = int(s) * int(s1)
                    a1 += en
        matriz.append(a)
        b=[]
        a1 = 0
        for i in range(2):
            if i == 1:
                b.append(a1)
            for j in range(2):
                s = self.celdas[i][j]
                s1 = other.celdas[j][1]
                en = int(s) * int(s1)
                a1 += en
        a1 = 0
        for i in range(2):
            if i == 1:
                b.append(a1)
            for j in range(2):
                s = self.celdas[1][j]
                s1 = other.celdas[j][1]
                en = int(s) * int(s1)
                a1 += en
        matriz.append(b)
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s



if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)

           