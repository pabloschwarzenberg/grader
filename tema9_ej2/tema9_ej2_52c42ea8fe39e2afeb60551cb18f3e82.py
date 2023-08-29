class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for fila in self.celdas:
            s += " ".join(str(elemento) for elemento in fila) + "\n"
        return s

    def __mul__(self, otra_matriz):
        filas_self = len(self.celdas)
        columnas_self = len(self.celdas[0])
        filas_otra = len(otra_matriz.celdas)
        columnas_otra = len(otra_matriz.celdas[0])

        if columnas_self != filas_otra:
            raise ValueError("Las matrices no tienen dimensiones compatibles para la multiplicación.")

        resultado = []
        for i in range(filas_self):
            fila_resultado = []
            for j in range(columnas_otra):
                elemento = 0
                for k in range(filas_otra):
                    elemento += self.celdas[i][k] * otra_matriz.celdas[k][j]
                fila_resultado.append(elemento)
            resultado.append(fila_resultado)

        return Matriz(resultado)

           