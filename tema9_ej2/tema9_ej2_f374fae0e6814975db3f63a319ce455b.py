class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0] * columnas for _ in range(filas)]

    def __getitem__(self, indice):
        return self.datos[indice]

    def __setitem__(self, indice, valor):
        self.datos[indice] = valor

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las matrices no se pueden multiplicar")

        filas_resultado = self.filas
        columnas_resultado = otra_matriz.columnas
        resultado = Matriz(filas_resultado, columnas_resultado)

        for i in range(filas_resultado):
            for j in range(columnas_resultado):
                suma = 0
                for k in range(self.columnas):
                    suma += self[i][k] * otra_matriz[k][j]
                resultado[i][j] = suma

        return resultado
 