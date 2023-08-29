import codecs
def decodificador(mensaje):
    codigo = codecs.ascii_decode(mensaje)
    return codigo

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         