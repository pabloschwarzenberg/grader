def jerigonzo(string):
    translate =""
    for letra in string:
        translate += letra
        if letra.lower() in "aeiou":
            translate += "p" + letra
    return translate