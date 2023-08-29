def jerigonzo(palabra):
    x = ""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            x += letra
            x += "p"
        x += letra
    return x
         