class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos
        self.filas = len(elementos)
        self.columnas = len(elementos[0])

    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las matrices no se pueden multiplicar")

        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(otra_matriz.columnas):
                producto_punto = 0
                for k in range(self.columnas):
                    producto_punto += self.elementos[i][k] * otra_matriz.elementos[k][j]
                fila.append(producto_punto)
            resultado.append(fila)

        return Matriz(resultado)

