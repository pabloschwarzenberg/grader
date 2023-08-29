def jerigonzo(original):
    traducida = ""
    for letra in original:
        if letra.lower() in ["a", "e", "i", "o", "u"]:
            traducida += letra + "p" + letra
        else:
            traducida += letra
    return traducida

if __name__ == "__main__":
    pass
         