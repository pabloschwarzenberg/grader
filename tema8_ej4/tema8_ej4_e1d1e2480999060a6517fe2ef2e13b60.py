def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_letra = ord(letra.lower())
            if ascii_letra >= 97 and ascii_letra <= 109:
                nueva_letra = chr(ascii_letra + 13)
            else:
                nueva_letra = chr(ascii_letra - 13)
            resultado += nueva_letra.upper() if letra.isupper() else nueva_letra
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           