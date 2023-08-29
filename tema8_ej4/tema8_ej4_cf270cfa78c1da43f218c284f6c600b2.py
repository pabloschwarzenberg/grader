def rot13(palabra):
    resultado = ""

    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) + 13
                if codigo > ord('Z'):
                    codigo -= 26
                resultado += chr(codigo)
            else:
                codigo = ord(letra) + 13
                if codigo > ord('z'):
                    codigo -= 26
                resultado += chr(codigo)
        else:
            resultado += letra

    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
