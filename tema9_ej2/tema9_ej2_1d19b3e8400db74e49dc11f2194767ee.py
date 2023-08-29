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
        if isinstance(other, Matriz):
            if len(self.celdas[0]) != len(other.celdas):
                raise ValueError("Las matrices no tienen dimensiones compatibles para la multiplicación.")
            
            result = Matriz()
            for i in range(len(self.celdas)):
                fila_resultado = []
                for j in range(len(other.celdas[0])):
                    suma = 0
                    for k in range(len(self.celdas[0])):
                        suma += self.celdas[i][k] * other.celdas[k][j]
                    fila_resultado.append(suma)
                result.celdas.append(fila_resultado)
            
            return result
        else:
            raise TypeError("La operación de multiplicación solo es válida entre matrices.")


if __name__ == "__main__":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2 = Matriz([[5, 6], [7, 8]])

    resultado = matriz1 * matriz2
    print(resultado)
           