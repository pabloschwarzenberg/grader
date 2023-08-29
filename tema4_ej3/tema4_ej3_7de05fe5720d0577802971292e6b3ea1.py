def jerigonzo(palabra):
    trad=""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            trad+= letra
            trad+= "p"
        trad+= letra
    return trad