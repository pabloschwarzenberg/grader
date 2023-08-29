def jerigonzo(string):
    palabra = ""
    for letra in string:
        palabra += letra
        if letra.lower() in "aeiou":
            palabra += "p" + letra
    return palabra
    mensaje= jerigonzo('esto es para vosotros aficion, siuuuu')
    print(mensaje)
    return string

if __name__ == "__main__":
    pass
         