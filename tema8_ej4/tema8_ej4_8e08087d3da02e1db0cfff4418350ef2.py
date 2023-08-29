def rot13(palabra):
    palabra_encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_code = (ord(letra) - ord('A') + 13) % 26 + ord('A')
                palabra_encriptada += chr(ascii_code)
            else:
                ascii_code = (ord(letra) - ord('a') + 13) % 26 + ord('a')
                palabra_encriptada += chr(ascii_code)
        else:
            palabra_encriptada += letra
    return palabra_encriptada

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
