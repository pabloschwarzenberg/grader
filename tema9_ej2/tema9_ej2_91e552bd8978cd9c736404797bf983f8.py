class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0] * columnas for _ in range(filas)]

    def ingresar_valor(self, fila, columna, valor):
        self.datos[fila][columna] = valor

    def obtener_valor(self, fila, columna):
        return self.datos[fila][columna]

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no son compatibles.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas)
        
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otra_matriz.datos[k][j]
                resultado.ingresar_valor(i, j, suma)
        
        return resultado
