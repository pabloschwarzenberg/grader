def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if 'a' <= letra <= 'z':
            nueva_letra = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= letra <= 'Z':
            nueva_letra = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
        else:
            nueva_letra = letra
        resultado += nueva_letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
