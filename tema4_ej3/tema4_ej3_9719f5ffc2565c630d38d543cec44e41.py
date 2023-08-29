def jerigonzo(palabra):
    traducida = ""
    for letra in palabra:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida        