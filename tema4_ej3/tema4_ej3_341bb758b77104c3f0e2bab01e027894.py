def jerigonzo(palabra):
    x = ""
    for letra in palabra:
        if letra in "AaEeIiOoUu":
            x += letra
            x += "p"
        x += letra
    return x

