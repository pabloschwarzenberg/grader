def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) + 13
                if codigo > ord('Z'):
                    codigo -= 26
                letra_encriptada = chr(codigo)
            else:
                codigo = ord(letra) + 13
                if codigo > ord('z'):
                    codigo -= 26
                letra_encriptada = chr(codigo)
        else:
            letra_encriptada = letra
        palabra_encriptada += letra_encriptada
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
