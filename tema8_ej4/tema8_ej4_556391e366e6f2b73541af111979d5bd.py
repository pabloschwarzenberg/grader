def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                ascii_code = ord(letra) - ord('a')
                encriptado = (ascii_code + 13) % 26
                resultado += chr(encriptado + ord('a'))
            else:
                ascii_code = ord(letra) - ord('A')
                encriptado = (ascii_code + 13) % 26
                resultado += chr(encriptado + ord('A'))
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
