def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            codigo = ord(letra)
            if letra.islower():
                codigo_encriptado = (codigo - ord('a') + 13) % 26 + ord('a')
            else:
                codigo_encriptado = (codigo - ord('A') + 13) % 26 + ord('A')
            encriptada += chr(codigo_encriptado)
        else:
            encriptada += letra
    return encriptada


if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)