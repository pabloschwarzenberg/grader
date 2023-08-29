def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                ascii_code = ord(letra)
                encrypted_code = (ascii_code - 97 + 13) % 26 + 97
                resultado += chr(encrypted_code)
            else:
                ascii_code = ord(letra)
                encrypted_code = (ascii_code - 65 + 13) % 26 + 65
                resultado += chr(encrypted_code)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)