def jerigonzo(string):
    c = []
    for p in string:
        for letra in p:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            c.append(letra)
    c = "".join(c)
    return c
         