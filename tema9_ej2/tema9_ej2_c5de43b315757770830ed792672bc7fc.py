class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[0])):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("Las matrices no se pueden multiplicar debido a dimensiones incompatibles.")
        
        # Crear matriz resultante con celdas llenas de ceros
        rows_a = len(self.celdas)
        cols_a = len(self.celdas[0])
        cols_b = len(other.celdas[0])
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        # Realizar multiplicación de matrices
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]
        
        return Matriz(result)

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
