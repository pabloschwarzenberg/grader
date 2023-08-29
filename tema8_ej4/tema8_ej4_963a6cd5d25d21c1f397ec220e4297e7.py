def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            nuevo_caracter = chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= caracter <= 'Z':
            nuevo_caracter = chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado
           