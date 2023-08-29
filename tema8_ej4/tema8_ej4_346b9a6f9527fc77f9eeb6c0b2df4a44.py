def rot13(palabra):
    resultado = ''
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                codigo = ord(caracter) - ord('A')
                encriptado = (codigo + 13) % 26
                resultado += chr(encriptado + ord('A'))
            else:
                codigo = ord(caracter) - ord('a')
                encriptado = (codigo + 13) % 26
                resultado += chr(encriptado + ord('a'))
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
