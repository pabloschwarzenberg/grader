from this import s


class Matriz:
    def init(self,celdas=[]):
        self.celdas=celdas

    def repr(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def mul(self, other):
        return Matriz(self.celdas * other.celdas)


if name == "main":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)