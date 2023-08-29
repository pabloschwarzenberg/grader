def rot13(palabra):
    encriptada = ''

    for letra in palabra:
        if 'a' <= letra <= 'z':
            encriptada += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= letra <= 'Z':
            encriptada += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptada += letra

    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    encriptada = rot13(palabra)
    print("Palabra encriptada:", encriptada)

