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
        # Verificar que el número de columnas de la primera matriz coincide con el número de filas de la segunda matriz
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices. Dimensiones incompatibles.")

        # Crear una nueva matriz para almacenar el resultado de la multiplicación
        resultado = []
        for i in range(len(self.celdas)):
            fila = []
            for j in range(len(other.celdas[0])):
                elemento = 0
                for k in range(len(other.celdas)):
                    elemento += self.celdas[i][k] * other.celdas[k][j]
                fila.append(elemento)
            resultado.append(fila)

        return Matriz(resultado)


# Ejemplo de uso
matriz1 = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matriz_resultado = matriz1 * matriz2
print(matriz_resultado)


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           