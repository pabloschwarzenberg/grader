class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]
    
    def __str__(self):
        return '\n'.join([' '.join([str(elemento) for elemento in fila]) for fila in self.matriz])
    
    def __mul__(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas)
        
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]
        
        return resultado
