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
            raise ValueError("Las matrices no son multiplicables.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas)
        
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otra_matriz.datos[k][j]
                resultado.datos[i][j] = suma
        
        return resultado
