def jerigonzo(palabra):
    lisVocal= []
    vocales=["a","e","i","o","u"]

    for c in palabra:
        lisVocal.append(c)
        if c in vocales:
            lisVocal.append("p")
            lisVocal.append(c)
        frase= "".join(lisVocal)
    return frase

print(jerigonzo("hola"))


if __name__ == "__main__":
    pass
         