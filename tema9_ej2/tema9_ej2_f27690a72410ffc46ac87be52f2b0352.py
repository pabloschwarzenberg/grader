class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas
    
    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[0])):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s
    
    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices: número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
        
        # Crear una matriz vacía del tamaño adecuado para el resultado
        filas_resultado = len(self.celdas)
        columnas_resultado = len(other.celdas[0])
        resultado = Matriz([[0] * columnas_resultado for _ in range(filas_resultado)])
        
        # Realizar la multiplicación de matrices
        for i in range(filas_resultado):
            for j in range(columnas_resultado):
                suma = 0
                for k in range(len(self.celdas[0])):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                resultado.celdas[i][j] = suma
        
        return resultado
