def jerigonzo(string):
    Palabra = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            Palabra.append(letra)
    Palabra = "".join(Palabra)
    return Palabra