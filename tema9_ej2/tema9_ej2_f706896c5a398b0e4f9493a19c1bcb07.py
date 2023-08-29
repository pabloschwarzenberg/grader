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
        mr=[]
        n_filas_m1=len(self.celdas)
        n_rows_m2=len(other.celdas[0])

        for row in range(n_filas_m1):
            mr_r=[]
            for col in range(n_rows_m2):
                s=0
                for row_2 in range(len(other.celdas)):
                    s+=self.celdas[row][row_2]*other.celdas[row_2][col]
                mr_r.append(s)
            mr.append(mr_r)
        return mr
            

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           