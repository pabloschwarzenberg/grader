def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_valor = ord(letra)
            if letra.islower():
                ascii_base = ord('a')
                encriptada += chr((ascii_valor - ascii_base + 13) % 26 + ascii_base)
            else:
                ascii_base = ord('A')
                encriptada += chr((ascii_valor - ascii_base + 13) % 26 + ascii_base)
        else:
            encriptada += letra

    return encriptada

if __name__ == "__main__":
    # Solicitar la palabra al usuario
    palabra = input("Ingresa una palabra: ")

    # Encriptar la palabra utilizando ROT13
    palabra_encriptada = rot13(palabra)

    # Imprimir la palabra encriptada
    print("Palabra encriptada con ROT13:", palabra_encriptada)          