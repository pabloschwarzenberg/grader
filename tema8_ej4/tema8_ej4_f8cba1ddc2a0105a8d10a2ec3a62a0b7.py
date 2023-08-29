def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                resultado += chr((ord(letra) - 97 + 13) % 26 + 97)
            else:
                resultado += chr((ord(letra) - 65 + 13) % 26 + 65)
        else:
            resultado += letra
    return resultado