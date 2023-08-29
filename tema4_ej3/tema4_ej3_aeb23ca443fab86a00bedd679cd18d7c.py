def jerigonzo(string):
    jeri = []
    for texto in string:
        for letra in texto:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            jeri.append(letra)
    jeri = "".join(jeri)
    return jeri


         