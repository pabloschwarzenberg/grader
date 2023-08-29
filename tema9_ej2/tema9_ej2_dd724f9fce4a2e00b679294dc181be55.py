class Matriz:
    def __init__(self,celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas) != len(other.celdas):
          raise ValueError("Las matrices deben tener la misma dimension")
        resultado = []
        for i in range(len(self.celdas)):
          fila = []
          for j in range(len(self.celdas)):
            valor = 0
            for k in range(len(self.celdas)):
              valor += self.celdas[i][k] * other.celdas[k][j]
            fila.append(valor)
          resultado.append(fila)
       return Matriz(resultado)