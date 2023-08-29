def rot13(palabra):
    palabra_trans= ""
    for letra in palabra:
        letra = ord(letra) + 13
        if letra > 122:
            letra -= 26
            palabra_trans += chr(letra)
        else:
            palabra_trans += chr(letra)
    return palabra_trans


if __name__ == "__main__":
    pass