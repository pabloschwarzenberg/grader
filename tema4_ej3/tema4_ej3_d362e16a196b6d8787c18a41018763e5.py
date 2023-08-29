#jerigonzo
def jerigonzo(string):
    aux = ""
    for letra in string:
        aux += letra
        if letra.lower() in "aeiou":
            aux += "p" + letra
    return aux
    return string
    