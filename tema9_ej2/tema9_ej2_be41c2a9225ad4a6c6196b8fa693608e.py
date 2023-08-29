class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.data = [[0] * columnas for _ in range(filas)]

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las matrices no son multiplicables")

        resultado = Matriz(self.filas, otra_matriz.columnas)

        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.data[i][j] += self.data[i][k] * otra_matriz.data[k][j]

        return resultado

    def asignar_valor(self, fila, columna, valor):
        self.data[fila][columna] = valor

    def obtener_valor(self, fila, columna):
        return self.data[fila][columna]

    def imprimir(self):
        for fila in self.data:
            print(fila)

# Ejemplo de uso
matriz1 = Matriz(2, 3)
matriz1.asignar_valor(0, 0, 1)
matriz1.asignar_valor(0, 1, 2)
matriz1.asignar_valor(0, 2, 3)
matriz1.asignar_valor(1, 0, 4)
matriz1.asignar_valor(1, 1, 5)
matriz1.asignar_valor(1, 2, 6)

matriz2 = Matriz(3, 2)
matriz2.asignar_valor(0, 0, 7)
matriz2.asignar_valor(0, 1, 8)
matriz2.asignar_valor(1, 0, 9)
matriz2.asignar_valor(1, 1, 10)
matriz2.asignar_valor(2, 0, 11)
matriz2.asignar_valor(2, 1, 12)

matriz_resultado = matriz1 * matriz2
matriz_resultado.imprimir()
