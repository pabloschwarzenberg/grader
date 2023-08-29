def jerigonzo(string):
    convertidor = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertidor.append(letra)
    convertidor = "".join(convertidor)
    return convertidor