def rot13(palabra):
    resultado=""
    for letra in palabra:
        cifrado=ord(letra)+13
        if cifrado>122:
            cifrado-=26
        resultado+=chr(cifrado)
        print(resultado)
    return resultado
