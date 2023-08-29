abcedario ="abcdefghijklmnopqrstuvwxyz"
cambio="nopqrstuvwxyzabcdefghijklm"
def rot13(palabra):
    cifrado = palabra.translate(palabra.maketrans(abcedario,cambio))
    return cifrado
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
