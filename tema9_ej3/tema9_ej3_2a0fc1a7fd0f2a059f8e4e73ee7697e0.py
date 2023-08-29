class ConversorBinario:
    def __init__(self):
        self.resultado = ''

    def convertir(self, texto):
        for letra in texto:
            codigo_binario = bin(ord(letra))[2:]
            self.resultado += codigo_binario + ','
        return self.resultado[:-1]