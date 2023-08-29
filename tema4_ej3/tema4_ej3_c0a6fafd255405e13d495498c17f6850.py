def jerigonzo(org):
    traductor = ""
    for letra in org:
        traductor += letra
        if letra.lower() in "aeiou":
            traductor += "p" + letra
    return traductor