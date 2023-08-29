def jerigonzo(string):
    convertida = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertida.append(letra)
    convertida = "".join(convertida)
    return convertida