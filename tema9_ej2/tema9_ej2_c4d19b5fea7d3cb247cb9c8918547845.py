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

        mr = []
        filai = []
        i = 0
        j = 0
        d1 = len(self.celdas)
        d2 = len(other.celdas)

        for i in range(d1):

            for j in range(d1):

                sumy = 0
                y = 0
                listaxi = []
                for k in range(d1):

                    sumy = sumy + self.celdas[i][k] * other.celdas[k][j]
                    listaxi.append(sumy)

                    if len(listaxi) == d1:

                        filai.append(sumy)
                        listaxi = []

                    else:

                        continue

        r = 0
        while r < len(filai):
            listoco = []
            listoco.append(filai[r:r + d1])
            mr.append(listoco)
            r = r + d1

            if (len(mr) >= d1):
                r = len(filai)
        
        mr = [mr[0][0],mr[1][0]]
        return Matriz(mr)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           