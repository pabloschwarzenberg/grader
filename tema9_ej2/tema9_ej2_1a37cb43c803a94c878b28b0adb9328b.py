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
        # Get the number of rows and columns of the matrices
        rows_self = len(self.celdas)
        columns_other = len(other.celdas[0])

        # Create a new matrix filled with zeros
        result = Matriz([[0 for _ in range(columns_other)] for _ in range(rows_self)])

        # Multiply the matrices
        for i in range(rows_self):
            for j in range(columns_other):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
