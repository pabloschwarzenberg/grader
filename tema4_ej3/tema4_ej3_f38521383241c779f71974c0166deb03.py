def jerigonzo(string):
    a = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            a += letra
            a += "p"
        a += letra
    return a
