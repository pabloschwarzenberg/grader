def jerigonzo(stringss):
    letrasMas = ""
    for letra in stringss:
        if letra in "aeiou":
            letrasMas += letra
            letrasMas += "p"
        letrasMas += letra
    return letrasMas