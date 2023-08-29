def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                encriptada = chr((ord(letra) - 97 + 13) % 26 + 97)
            else:
                encriptada = chr((ord(letra) - 65 + 13) % 26 + 65)
            resultado += encriptada
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           