def jerigonzo(string):
    translate = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            translate += letra
            translate += "p"
        translate += letra
    return translate


if __name__ == "__main__":
    pass
         