def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_letra = ord(letra)
            if letra.islower():
                encriptada += chr((ascii_letra - 97 + 13) % 26 + 97)
            else:
                encriptada += chr((ascii_letra - 65 + 13) % 26 + 65)
        else:
            encriptada += letra
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
