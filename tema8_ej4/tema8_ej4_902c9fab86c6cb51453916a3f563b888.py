def rot13(palabra):
    encriptada = ""
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                encriptada += chr((ord(caracter) - 65 + 13) % 26 + 65)
            else:
                encriptada += chr((ord(caracter) - 97 + 13) % 26 + 97)
        else:
            encriptada += caracter
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingrese la palabra a encriptar: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:")
    print(palabra_encriptada)
           