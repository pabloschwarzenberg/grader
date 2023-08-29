def rot13(palabra):
    encriptada = ""
    for char in palabra:
        if char.isalpha():
            ascii_value = ord(char.lower())
            if ascii_value >= 97 and ascii_value <= 109:
                encriptada += chr(ascii_value + 13)
            else:
                encriptada += chr(ascii_value - 13)
        else:
            encriptada += char
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
