def rot13(palabra):
    palabra_encriptada = ""
    for caracter in palabra:
        if caracter.isalpha():
            ascii_value = ord(caracter)
            if caracter.islower():
                ascii_value = (ascii_value - 97 + 13) % 26 + 97
            else:
                ascii_value = (ascii_value - 65 + 13) % 26 + 65
            caracter_encriptado = chr(ascii_value)
            palabra_encriptada += caracter_encriptado
        else:
            palabra_encriptada += caracter
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
           