def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                ascii_value = ord(letra)
                encripted_ascii = (ascii_value - 97 + 13) % 26 + 97
                resultado += chr(encripted_ascii)
            else:
                ascii_value = ord(letra)
                encripted_ascii = (ascii_value - 65 + 13) % 26 + 65
                resultado += chr(encripted_ascii)
        else:
            resultado += letra
    return resultado
