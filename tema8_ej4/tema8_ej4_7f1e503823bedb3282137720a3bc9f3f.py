def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                encriptada += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                encriptada += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptada += letra
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
