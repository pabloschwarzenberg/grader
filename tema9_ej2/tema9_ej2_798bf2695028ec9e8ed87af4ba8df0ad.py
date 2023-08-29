class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no son compatibles.")
        
        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                sum = 0
                for k in range(len(self.celdas[0])):
                    sum += self.celdas[i][k] * other.celdas[k][j]
                row.append(sum)
            result.append(row)
        
        return Matriz(result)


# Ejemplo de uso
matriz1 = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = Matriz([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

resultado = matriz1 * matriz2

print("Resultado de la multiplicación:")
print(resultado)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           