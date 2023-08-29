class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0] * columnas for _ in range(filas)]
    
    def __str__(self):
        matriz_str = ""
        for fila in self.datos:
            matriz_str += " ".join(str(elemento) for elemento in fila) + "\n"
        return matriz_str
    
    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas)
        
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otra_matriz.datos[k][j]
                resultado.datos[i][j] = suma
        
        return resultado
matriz1 = Matriz(2, 3)
matriz1.datos = [[1, 2, 3], [4, 5, 6]]

matriz2 = Matriz(3, 2)
matriz2.datos = [[7, 8], [9, 10], [11, 12]]

resultado = matriz1 * matriz2
print(resultado)
