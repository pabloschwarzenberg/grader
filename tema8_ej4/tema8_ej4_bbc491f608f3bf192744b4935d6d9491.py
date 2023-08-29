def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_value = ord(letra)
                shifted_value = (ascii_value - 65 + 13) % 26 + 65
                resultado += chr(shifted_value)
            else:
                ascii_value = ord(letra)
                shifted_value = (ascii_value - 97 + 13) % 26 + 97
                resultado += chr(shifted_value)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)