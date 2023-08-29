def jerigonzo(string):
    P = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            P.append(letra)
    READY = "".join(P)
    return READY

         