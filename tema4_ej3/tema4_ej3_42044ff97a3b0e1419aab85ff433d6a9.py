def jerigonzo(string):
    convertido = []
    for termino in string:
        for letra in termino:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido