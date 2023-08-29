def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_value = ord(letra)
            if letra.islower():
                encripted_value = (ascii_value - 97 + 13) % 26 + 97
            else:
                encripted_value = (ascii_value - 65 + 13) % 26 + 65
            palabra_encriptada += chr(encripted_value)
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
