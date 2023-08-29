def rot13(palabra):
    palabra = list(palabra)
    for posicion in range(len(palabra)):
        if palabra[posicion] in "abcdefghijklm":
            num = ord(palabra[posicion]) + 13
        elif palabra[posicion] in "nopqrstuvwxyz":
            num = ord(palabra[posicion]) - 13
        palabra[posicion] = chr(num)
    palabra = "".join(palabra)
    return palabra