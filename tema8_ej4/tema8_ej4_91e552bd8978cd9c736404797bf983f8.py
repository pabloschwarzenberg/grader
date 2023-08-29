def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_code = ord(letra) - ord('A')
                encriptado = (ascii_code + 13) % 26 + ord('A')
                resultado += chr(encriptado)
            else:
                ascii_code = ord(letra) - ord('a')
                encriptado = (ascii_code + 13) % 26 + ord('a')
                resultado += chr(encriptado)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)
