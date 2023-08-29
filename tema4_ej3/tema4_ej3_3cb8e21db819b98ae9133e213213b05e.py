def jerigonzo(string):
    jerigonzo = ""
    for letra in string:
        if letra.lower() in "aeiouáéíóú":
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    pass
         