def rot13(palabra):
    encriptado = ""
    for char in palabra:
        if char.isalpha():
            if char.isupper():
                encriptado += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                encriptado += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            encriptado += char
    return encriptado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           