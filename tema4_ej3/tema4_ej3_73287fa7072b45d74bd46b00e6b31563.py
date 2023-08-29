def esVocal(string):
    return string.upper() in "AEIOU" and len(string)==1


def jerigonzo (string):
    aux = ""
    for letra in string:
        if not esVocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
    return aux