def rot13(palabra):
    encriptado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                encriptado += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                encriptado += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptado += letra
    return encriptado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           