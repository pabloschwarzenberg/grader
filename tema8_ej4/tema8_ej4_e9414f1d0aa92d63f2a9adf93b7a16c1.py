def rot13(palabra):
    palabra_encriptada = ""

    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                nueva_letra = chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                nueva_letra = chr((ord(letra) - 97 + 13) % 26 + 97)
            palabra_encriptada += nueva_letra
        else:
            palabra_encriptada += letra

    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
