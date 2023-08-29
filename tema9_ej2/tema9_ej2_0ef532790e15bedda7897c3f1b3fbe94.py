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

    def __mul__(self, a, b): 
        mr=[]
        i=0
        j=0
        d1=len(a)
        d2=len(b)
        if d1!=d2:
            print("Las matrices no se pueden multiplicar porque no tienen la misma dimension")
            return mr
        elif d1==d2:
            while i<d1:
                filai=[]
                while j<d1:
                    mij=a[i][j]*b[i][j]
                    filai.append(mij)
                    j=j+1
                mr.append(filai)
                i=i+1
                j=0
            return mr

    matriz1=[]
    matriz2=[]
    contador=0

    dimension=4
    print("Ingrese los elementos de la fila de la matriz separados por comas")
    while contador < dimension:
        fila_a=[1,2]
        fila_b=[5,6]
        contador=contador+1

      


    print(matriz1)
    print(matriz2)
    mr=__mul__(self,matriz1,matriz2)
    print(mr)


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           