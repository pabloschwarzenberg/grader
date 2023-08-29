def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                encriptada += chr((ord(letra) - 65 + 13) % 26 + 65)
            else:
                encriptada += chr((ord(letra) - 97 + 13) % 26 + 97)
        else:
            encriptada += letra
    return encriptada