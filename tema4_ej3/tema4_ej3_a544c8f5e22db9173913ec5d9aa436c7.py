def jerigonzo(string):
    palabra = ""
    for letra in string:
        palabra += letra
        if letra.lower() in "aeiou":
            palabra += "p" + letra
    return palabra

if __name__ == "__main__":
    pass
         