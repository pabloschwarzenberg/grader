def jerigonzo(string):
    jerigonzo = ""
    for letra in string:
        if letra.lower() in ["a", "e", "i", "o", "u"]:
            jerigonzo += letra + "p" + letra
        else:
            jerigonzo += letra
    return jerigonzo

if __name__=="__main__":
    pass
