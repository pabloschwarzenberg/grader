def rot13(palabra):
    encriptado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                encriptado += chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                encriptado += chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            encriptado += letra
    return encriptado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           