def jerigonzo(string):
    traduccion = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            traduccion.append(letra)
    traduccion = "".join(traduccion)
    return traduccion
