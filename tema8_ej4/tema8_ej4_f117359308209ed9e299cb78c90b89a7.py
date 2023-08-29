def rot13(palabra):
    encriptado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                encriptado += chr((ord(letra) - 97 + 13) % 26 + 97)
            else:
                encriptado += chr((ord(letra) - 65 + 13) % 26 + 65)
        else:
            encriptado += letra
    return encriptado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
