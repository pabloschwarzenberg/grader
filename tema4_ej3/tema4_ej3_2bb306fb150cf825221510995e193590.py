def jerigonzo(string):
    interprete = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            interprete.append(letra)
    interprete = "".join(interprete)
    return interprete