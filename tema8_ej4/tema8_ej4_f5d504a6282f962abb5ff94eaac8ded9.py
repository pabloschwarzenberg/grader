def rot13(palabra):
    encriptada = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                encriptada += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
            else:
                encriptada += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
        else:
            encriptada += letra
    return encriptada