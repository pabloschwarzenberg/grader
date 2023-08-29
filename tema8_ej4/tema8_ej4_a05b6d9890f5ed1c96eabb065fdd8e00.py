def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_code = (ord(letra) - 65 + 13) % 26 + 65
            else:
                ascii_code = (ord(letra) - 97 + 13) % 26 + 97
            resultado += chr(ascii_code)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)