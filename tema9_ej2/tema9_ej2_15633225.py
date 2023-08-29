class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    

    def __mul__(self, other):
        t=[[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
              for k in range(2):
                t[i][j]+=(self.celdas[i][k])*(other.celdas[k][j])
        return t


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           