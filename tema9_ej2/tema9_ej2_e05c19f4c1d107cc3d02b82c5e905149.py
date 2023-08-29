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
        new = []
        a = self.celdas
        b = list(zip(*other.celdas))

        for i in range(len(a)):
            new.append([])
            sum = 0
            for k in range(len(b)):
                for j in range(len(a[i])):
                    sum += a[i][j] * b[k][j]
                new[i].append(sum)
                sum = 0
        
        return Matriz(new)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           
