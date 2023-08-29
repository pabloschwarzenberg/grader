def jerigonzo(string):
    traducida = ""
    for letra in string:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida

if __name__ == "_main_":
    pass