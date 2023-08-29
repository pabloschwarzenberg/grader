class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0] * columnas for _ in range(filas)]

    def __str__(self):
        matriz_str = ""
        for fila in self.datos:
            fila_str = " ".join(str(elemento) for elemento in fila)
            matriz_str += fila_str + "\n"
        return matriz_str

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otra_matriz.datos[k][j]
                resultado.datos[i][j] = suma

        return resultado

if __name__ == "__main__":
    matriz1 = Matriz(2, 2)
    matriz1.datos = [[1, 2], [3, 4]]

    matriz2 = Matriz(2, 2)
    matriz2.datos = [[5, 6], [7, 8]]

    matriz_resultado = matriz1 * matriz2
    print(matriz_resultado)
