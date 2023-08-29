def rot13(palabra):
    palabra = list(palabra)
    for i in range(len(palabra)):
        l = palabra[i]
        if 'A' <= l <= 'Z':
            palabra[i] = chr((ord(l) + 13 - 65) % 26 + 65)
        else:
            palabra[i] = chr((ord(l) + 13 - 97) % 26 + 97)

    return ''.join(palabra)