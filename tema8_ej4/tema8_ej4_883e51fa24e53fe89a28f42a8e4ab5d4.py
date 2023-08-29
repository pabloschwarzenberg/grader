def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_inicio = ord('A')
            else:
                ascii_inicio = ord('a')
            ascii_letra = ord(letra)
            nueva_letra = chr((ascii_letra - ascii_inicio + 13) % 26 + ascii_inicio)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado