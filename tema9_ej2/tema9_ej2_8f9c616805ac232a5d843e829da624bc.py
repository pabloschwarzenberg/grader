class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        # Verificar si other es una instancia de la clase Matriz
        if isinstance(other, Matriz):
            # Verificar si las dimensiones de las matrices son compatibles para la multiplicación
            if len(self.celdas[0]) == len(other.celdas):
                # Crear una nueva matriz para almacenar el resultado de la multiplicación
                resultado = []
                filas_self = len(self.celdas)
                columnas_self = len(self.celdas[0])
                columnas_other = len(other.celdas[0])

                for i in range(filas_self):
                    fila = []
                    for j in range(columnas_other):
                        suma = 0
                        for k in range(columnas_self):
                            suma += self.celdas[i][k] * other.celdas[k][j]
                        fila.append(suma)
                    resultado.append(fila)

                # Devolver una nueva instancia de la clase Matriz con el resultado de la multiplicación
                return Matriz(resultado)
            else:
                raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
        else:
            raise TypeError("El operando de la multiplicación debe ser una instancia de la clase Matriz")

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
