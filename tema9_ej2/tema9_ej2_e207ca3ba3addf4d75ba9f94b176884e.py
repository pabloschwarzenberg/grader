class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no son compatibles.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]

        return resultado

    def mostrar(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
matriz1 = Matriz(2, 3)
matriz1.matriz = [[1, 2, 3], [4, 5, 6]]

matriz2 = Matriz(3, 2)
matriz2.matriz = [[7, 8], [9, 10], [11, 12]]

resultado = matriz1 * matriz2
resultado.mostrar()
