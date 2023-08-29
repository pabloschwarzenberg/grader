def jerigonzo(string):
    traducida = ""
    for x in string:
        traducida += x
        if x.lower() in "aeiou":
            traducida += "p" + x
    return traducida

if name == "main":
    jerigonzo()