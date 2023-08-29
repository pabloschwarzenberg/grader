def rot13(palabra):
    contador = 0
    palabrareturn = ""
    cifrado = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z'}

    for i in palabra:
        if i in cifrado.keys():
            palabrareturn = palabrareturn + cifrado[i]
        else:
            for e in cifrado:
                if cifrado[e] == i:
                    palabrareturn = palabrareturn + e
    return palabrareturn           