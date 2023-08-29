def jerigonzo(string):
    resultado=""
    string=string.lower()
    vocales=["a","e","i","o","u"]
    for i in string:
        if i in vocales:
            resultado=resultado+i+"p"+i
        else:
            resultado=resultado+i
    return resultado
