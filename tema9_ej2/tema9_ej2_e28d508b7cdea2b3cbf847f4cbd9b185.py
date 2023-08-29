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
    def matriz_lista(self):
        

    def __mul__(self, other):
        s=[]
        for i in range(len(self.celdas)):
            for celdas in self:
              for c in other:
                s.append(int(celdas[i][0])*int(c[i][0]))
                s.append(int(celdas[i][1])*int(c[i][1]))
        return s

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           