def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.islower():
                encriptado = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
            else:
                encriptado = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptado = caracter
        resultado += encriptado
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
