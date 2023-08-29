#Encriptador ROT13
def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if 'a' <= letra <= 'z':
            resultado += chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= letra <= 'Z':
            resultado += chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            resultado += letra
    return resultado