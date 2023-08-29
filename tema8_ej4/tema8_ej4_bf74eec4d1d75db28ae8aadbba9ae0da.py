def rot13(palabra):
    encriptador =""
    palabra1 = palabra.lower()
    for i in palabra1:
        if i == "a":
            i = "n"
            encriptador = encriptador + i
        elif i == "b":
            i = "o"
            encriptador = encriptador + i
        elif i == "c":
            i = "p"
            encriptador = encriptador + i
        elif i == "d":
            i = "q"
            encriptador = encriptador + i
        elif i == "e":
            i = "r"
            encriptador = encriptador + i
        elif i == "f":
            i = "s"
            encriptador = encriptador + i
        elif i == "g":
            i = "t"
            encriptador = encriptador + i
        elif i == "h":
            i = "u"
            encriptador = encriptador + i
        elif i == "i":
            i = "v"
            encriptador = encriptador + i
        elif i == "j":
            i = "w"
            encriptador = encriptador + i
        elif i == "k":
            i = "x"
            encriptador = encriptador + i
        elif i == "l":
            i = "y"
            encriptador = encriptador + i
        elif i == "m":
            i = "z"
            encriptador = encriptador + i
        elif i == "n":
            i = "a"
            encriptador = encriptador + i
        elif i == "o":
            i = "b"
            encriptador = encriptador + i
        elif i == "p":
            i = "c"
            encriptador = encriptador + i
        elif i == "q":
            i = "d"
            encriptador = encriptador + i
        elif i == "r":
            i = "e"
            encriptador = encriptador + i
        elif i == "s":
            i = "f"
            encriptador = encriptador + i
        elif i == "t":
            i = "g"
            encriptador = encriptador + i
        elif i == "u":
            i = "h"
            encriptador = encriptador + i
        elif i == "v":
            i = "i"
            encriptador = encriptador + i
        elif i == "w":
            i = "j"
            encriptador = encriptador + i
        elif i == "x":
            i = "k"
            encriptador = encriptador + i
        elif i == "y":
            i = "l"
            encriptador = encriptador + i
        elif i == "z":
            i = "m"
            encriptador = encriptador + i
    return encriptador