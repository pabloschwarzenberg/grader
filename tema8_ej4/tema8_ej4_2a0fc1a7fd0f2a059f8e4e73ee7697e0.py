def rot13(palabra):
    resultado = ''
    for letra in palabra:
        if letra.isalpha():
            ascii_letra = ord(letra)
            if letra.isupper():
                ascii_letra = (ascii_letra - 65 + 13) % 26 + 65
            else:
                ascii_letra = (ascii_letra - 97 + 13) % 26 + 97
            resultado += chr(ascii_letra)
        else:
            resultado += letra
    return resultado
