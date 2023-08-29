def jerigonzo(string):
    cuerda = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            cuerda.append(letra)
    cuerda = "".join(cuerda)
    return cuerda