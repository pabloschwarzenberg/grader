def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if caracter.isalpha():
            ascii_value = ord(caracter.lower())
            encriptado = chr((ascii_value - 97 + 13) % 26 + 97)
            resultado += encriptado.upper() if caracter.isupper() else encriptado
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           