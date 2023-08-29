def decodificar(mensaje):
    numeros_binarios = mensaje.split(",")
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]
    mensaje_decodificado = "".join(letras)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)


# multiplicacion de matrices

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
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")
        
        resultado = []
        for i in range(len(self.celdas)):
            fila = []
            for j in range(len(other.celdas[0])):
                elemento = 0
                for k in range(len(other.celdas)):
                    elemento += self.celdas[i][k] * other.celdas[k][j]
                fila.append(elemento)
            resultado.append(fila)
        
        return Matriz(resultado)

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)