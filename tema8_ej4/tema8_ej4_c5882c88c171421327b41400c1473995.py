import codecs

def rot13(palabra):
    return codecs.encode(palabra, 'rot13')

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           