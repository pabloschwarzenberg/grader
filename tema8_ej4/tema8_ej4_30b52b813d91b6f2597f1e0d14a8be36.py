def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            codigo = ord(letra)
            if letra.isupper():
                codigo_encriptado = (codigo - 65 + 13) % 26 + 65
            else:
                codigo_encriptado = (codigo - 97 + 13) % 26 + 97
            letra_encriptada = chr(codigo_encriptado)
        else:
            letra_encriptada = letra
        palabra_encriptada += letra_encriptada
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
