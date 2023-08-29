def jerigonzo(string):
    mod = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            mod.append(letra)
    mod = "".join(mod)
    return mod

if __name__ == "__main__":
    pass
         