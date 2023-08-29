def rot13(palabra):
    resultado = ""
    for char in palabra:
        if char.isalpha():
            if char.isupper():
                encriptado = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                encriptado = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            resultado += encriptado
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
