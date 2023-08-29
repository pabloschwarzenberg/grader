class Matriz:
    def __init__(self, datos):
        self.datos = datos

    def __mul__(self, otra_matriz):
        if len(self.datos[0]) != len(otra_matriz.datos):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")

        filas_self = len(self.datos)
        columnas_self = len(self.datos[0])
        filas_otra = len(otra_matriz.datos)
        columnas_otra = len(otra_matriz.datos[0])

        # Crear una matriz resultado llena de ceros
        resultado = [[0] * columnas_otra for _ in range(filas_self)]

        # Realizar la multiplicación de matrices
        for i in range(filas_self):
            for j in range(columnas_otra):
                for k in range(columnas_self):
                    resultado[i][j] += self.datos[i][k] * otra_matriz.datos[k][j]

        return Matriz(resultado)
        
if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           