class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        # Validar que las matrices sean del mismo tamaño
        if len(self.celdas) != len(other.celdas):
            return None # Retornar None si no se puede multiplicar
        # Crear una matriz vacía para guardar el resultado
        resultado = Matriz([[0 for j in range(len(self.celdas))] for i in range(len(self.celdas))])
        # Recorrer las filas de la primera matriz con un ciclo for
        for i in range(len(self.celdas)):
            # Recorrer las columnas de la segunda matriz con otro ciclo for
            for j in range(len(other.celdas)):
                # Recorrer las columnas de la primera matriz o las filas de la segunda matriz con otro ciclo for
                for k in range(len(self.celdas)):
                    # Sumar el producto de los elementos correspondientes y asignarlo a la celda del resultado
                    resultado.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]
        # Retornar el resultado como el producto de las matrices
        return resultado

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
