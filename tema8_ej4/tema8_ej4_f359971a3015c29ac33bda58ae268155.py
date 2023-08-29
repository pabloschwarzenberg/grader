import codecs


def rot13(palabra):
    trad = codecs.encode(palabra, 'rot13')
    return trad


if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
