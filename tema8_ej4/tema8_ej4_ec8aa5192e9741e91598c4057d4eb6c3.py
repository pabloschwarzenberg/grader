def rot13(palabra):
    palabra_encriptada = ""
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.islower():
                codigo = ord(caracter) - 97
                codigo_encriptado = (codigo + 13) % 26
                caracter_encriptado = chr(codigo_encriptado + 97)
                palabra_encriptada += caracter_encriptado
            else:
                codigo = ord(caracter) - 65
                codigo_encriptado = (codigo + 13) % 26
                caracter_encriptado = chr(codigo_encriptado + 65)
                palabra_encriptada += caracter_encriptado
        else:
            palabra_encriptada += caracter
    return palabra_encriptada

if __name__ == "__main__":
    palabra_original = input("Ingrese la palabra a encriptar: ")
    palabra_encriptada = rot13(palabra_original)
    print("Palabra encriptada: ", palabra_encriptada)
