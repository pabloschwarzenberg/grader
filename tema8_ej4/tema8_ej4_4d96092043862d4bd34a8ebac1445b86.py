def rot13(palabra):
    pa=""
    for i in (palabra):
        if i == "a":
            pa +="n"
        if i == "b":
            pa +="o"
        if i == "c":
            pa +="p"
        if i == "d":
            pa +="q"
        if i == "e":
            pa +="r"
        if i == "f":
            pa +="s"
        if i == "g":
            pa +="t"
        if i == "h":
            pa +="u"
        if i == "i":
            pa +="v"
        if i == "j":
            pa +="w"
        if i == "k":
            pa +="x"
        if i == "l":
            pa +="y"
        if i == "m":
            pa +="z"
        if i == "n":
            pa +="a"
        if i == "o":
            pa +="b"
        if i == "p":
            pa +="c"
        if i == "q":
            pa +="d"
        if i == "r":
            pa +="e"
        if i == "s":
            pa +="f"
        if i == "t":
            pa +="g"
        if i == "u":
            pa +="h"
        if i == "v":
            pa +="i"
        if i == "w":
            pa +="j"
        if i == "x":
            pa +="k"
        if i == "y":
            pa +="l"
        if i == "z":
            pa +="m"
    return pa
if __name__=="main_":
    palabra=str(input("Ingresa la palabra que quieras encriptar: "))
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           