def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios separados por comas
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a decimal y luego a su correspondiente letra
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir las letras para formar el mensaje descifrado
    mensaje_descifrado = "".join(letras)

    return mensaje_descifrado
def decodificar(mensaje):
    # Dividir el mensaje en una lista de números binarios separados por comas
    numeros_binarios = mensaje.split(",")

    # Convertir cada número binario a decimal y luego a su correspondiente letra
    letras = [chr(int(binario, 2)) for binario in numeros_binarios]

    # Unir las letras para formar el mensaje descifrado
    mensaje_descifrado = "".join(letras)

    return mensaje_descifrado
class Matriz:
    def init(self, celdas=[]):
        self.celdas = celdas

    def repr(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[i])):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s
