def rot13(palabra):
    import codecs
    codec=codecs.decode(palabra,"rot13")
    return codec

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           