def rot13(palabra):
    encriptada = ""

    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            encriptada += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            encriptada += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptada += caracter

    return encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
