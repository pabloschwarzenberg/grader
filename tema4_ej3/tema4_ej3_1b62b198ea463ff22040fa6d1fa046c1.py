def jerigonzo(string):
    jeri = []
    for palabra in string:
        for letra in palabra:
            if letra in "aAeEiIoOuU":
                letra = letra + "p"+ letra
            jeri.append(letra)
    jeri = "".join(jeri)
    return jeri


if __name__ == "__main__":
    pass
         