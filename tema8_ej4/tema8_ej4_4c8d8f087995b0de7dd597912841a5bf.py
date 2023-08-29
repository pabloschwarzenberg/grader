def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            encriptado = (ord(letra) - ascii_offset + 13) % 26 + ascii_offset
            resultado += chr(encriptado)
        else:
            resultado += letra
    return resultado
