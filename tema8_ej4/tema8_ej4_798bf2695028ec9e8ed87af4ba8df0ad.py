def rot13(palabra):
    encriptado = ""
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                encriptado += chr((ord(caracter) - 65 + 13) % 26 + 65)
            else:
                encriptado += chr((ord(caracter) - 97 + 13) % 26 + 97)
        else:
            encriptado += caracter
    return encriptado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada con ROT13:", palabra_encriptada)
