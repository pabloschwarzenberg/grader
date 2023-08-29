def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_value = ord(letra.lower())
            ascii_value_rot = (ascii_value - 97 + 13) % 26 + 97
            encriptada += chr(ascii_value_rot)
        else:
            encriptada += letra
    return encriptada

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palabra)
    print("El resultado es:", resultado)

           