def jerigonzo(string):
    traduccion = ""
    for letra in string:
        traduccion += letra
        if letra.lower() in "aeiou":
            traduccion += "p" + letra

    return traduccion
if __name__ == "__main__":
    pass
         