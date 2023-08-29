def jerigonzo(st):
    x = []
    for palabra in st:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            x.append(letra)
    x = "".join(x)
    return x
    return st
         