def rot13(palabra):
    encriptada = ""

    for letra in palabra:
        if letra.isalpha():
            encriptada += chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            encriptada += letra

    return encriptada
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           