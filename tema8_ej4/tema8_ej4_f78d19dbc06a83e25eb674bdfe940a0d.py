def rot13(palabra):
    resultado = ""

    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                nueva_letra = chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                nueva_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            nueva_letra = letra

        resultado += nueva_letra

    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")

    palabra_encriptada = rot13(palabra)

    print("Palabra encriptada:", palabra_encriptada)

