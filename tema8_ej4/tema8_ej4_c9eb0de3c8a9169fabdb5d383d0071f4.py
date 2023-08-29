def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_val = ord(letra)
            if letra.islower():
                ascii_val = (ascii_val - 97 + 13) % 26 + 97
            else:
                ascii_val = (ascii_val - 65 + 13) % 26 + 65
            resultado += chr(ascii_val)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese la palabra a encriptar: ")
    palabra_encriptada = rot13(palabra)
    print(palabra_encriptada)           