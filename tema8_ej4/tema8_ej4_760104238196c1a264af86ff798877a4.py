def rot13(palabra):
    palabra = list(palabra)
    for i in range(len(palabra)):
        letra = chr((ord(palabra[i]) - 97 + 13) % 26 + 97)
        palabra[i] = letra
    return ''.join(palabra)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           