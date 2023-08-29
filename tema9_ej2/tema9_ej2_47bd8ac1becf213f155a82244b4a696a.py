class Matriz:       #[[1,2],[3,4]]  x  [[5,6],[7,8]]
    def __init__(self,celdas=[]):     #     1     2            5    6                   1x5 + 2x7      1x6 + 2x8                19   22
        self.celdas=celdas                  #      3     4            7    8                   3x5+ 4x7      3x6 +  4x8                43   50

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self,other):
        resultado=[]
        for k in range(len(self.celdas)):
            resultado.append([0]*len(other.celdas[0]))
            for i in range(len(other.celdas[0])):
                resultado[k][i]=0
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[0])):
                for k in range(len(other.celdas[0])):
                    resultado[i][k]+=(self.celdas[i][j]*other.celdas[j][k])
                    r=Matriz(resultado)
        return r
        
                

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           
