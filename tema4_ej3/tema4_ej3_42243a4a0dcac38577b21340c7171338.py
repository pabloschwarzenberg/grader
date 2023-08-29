def jerigonzo(string):
    trad = ""
    for letra in string:
        trad += letra
        if letra.lower() in "aeiou":
            trad += "p" + letra
    return trad