def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                encriptada += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                encriptada += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            encriptada += letra
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)