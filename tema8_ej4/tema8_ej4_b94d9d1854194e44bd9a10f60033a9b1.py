def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            ascii_value = ord(letra)
            if letra.islower():
                ascii_value = (ascii_value - 97 + 13) % 26 + 97
            else:
                ascii_value = (ascii_value - 65 + 13) % 26 + 65
            resultado += chr(ascii_value)
        else:
            resultado += letra
    return resultado
