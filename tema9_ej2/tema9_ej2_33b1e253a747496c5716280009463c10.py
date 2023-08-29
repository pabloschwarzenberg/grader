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
        if isinstance(other, Matriz):
            if len(self.celdas) == len(other.celdas):
                resultado = Matriz()
                for i in range(len(self.celdas)):
                    resultado.celdas.append([])
                    for j in range(len(self.celdas)):
                        resultado.celdas[i].append(0)
                        for k in range(len(self.celdas)):
                            resultado.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]
                return resultado
            else:
                return None
        else:
            return None

if __name__ == "__main__":
    # Ejemplo de uso
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    print(a)
    print(b)
    r = a * b
    print(r)