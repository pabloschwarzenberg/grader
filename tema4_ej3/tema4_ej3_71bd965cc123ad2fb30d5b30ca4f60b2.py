def jerigonzo(original):
    traducida = ""
    for letra in original:
        traducida += letra
        if letra in "AEIOUaeiou":
            traducida += "p" + letra
    return traducida