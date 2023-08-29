def jerigonzo(string):
    renombrado = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            renombrado.append(letra)
    renombrado = "".join(renombrado)
    return renombrado