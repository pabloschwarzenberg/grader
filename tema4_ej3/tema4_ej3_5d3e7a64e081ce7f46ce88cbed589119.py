def jerigonzo(texto):
    t = ""
    for letra in texto:
        if letra in "AEIOUaeiou":
             t += letra
             t += "p"
        t += letra
    return t         