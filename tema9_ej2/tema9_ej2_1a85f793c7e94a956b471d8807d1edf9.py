class Matriz:
    def __init__(self, datos):
        self.filas = len(datos)
        self.columnas = len(datos[0])
        self.datos = datos
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.datos])
    
    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")

        resultado = Matriz([[0] * otra_matriz.columnas for _ in range(self.filas)])
        
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.datos[i][j] += self.datos[i][k] * otra_matriz.datos[k][j]
        
        return resultado


if __name__ == "__main__":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2 = Matriz([[5, 6], [7, 8]])
    resultado = matriz1 * matriz2

    print("Matriz 1:")
    print(matriz1)
    print()

    print("Matriz 2:")
    print(matriz2)
    print()

    print("Resultado de la multiplicación:")
    print(resultado)

