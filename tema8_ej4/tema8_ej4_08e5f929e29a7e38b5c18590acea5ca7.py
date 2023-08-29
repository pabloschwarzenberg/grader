import codecs
def rot13(palabra):
    resultado = codecs.encode(palabra, "rot_13")
    return resultado
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)