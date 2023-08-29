def rot13(palabra):
    l = list(palabra)
    texto = ""
    while len(l)>0:
        if l[0] == "a":
            texto = texto + "n"
            del l[0]
            continue
        if l[0] == "n":
            texto = texto + "a"
            del l[0]
            continue
        if l[0] == "b":
            texto = texto + "o"
            del l[0]
            continue
        if l[0] == "o":
            texto = texto + "b"
            del l[0]
            continue
        if l[0] == "c":
            texto = texto + "p"
            del l[0]
            continue
        if l[0] == "p":
            texto = texto + "c"
            del l[0]
            continue
        if l[0] == "q":
            texto = texto + "d"
            del l[0]
            continue
        if l[0] == "d":
            texto = texto + "q"
            del l[0]
            continue
        if l[0] == "e":
            texto = texto + "r"
            del l[0]
            continue
        if l[0] == "r":
            texto = texto + "e"
            del l[0]
            continue
        if l[0] == "f":
            texto = texto + "s"
            del l[0]
            continue
        if l[0] == "s":
            texto = texto + "f"
            del l[0]
            continue
        if l[0] == "g":
            texto = texto + "t"
            del l[0]
            continue
        if l[0] == "t":
            texto = texto + "g"
            del l[0]
            continue
        if l[0] == "h":
            texto = texto + "u"
            del l[0]
            continue
        if l[0] == "u":
            texto = texto + "h"
            del l[0]
            continue
        if l[0] == "i":
            texto = texto + "v"
            del l[0]
            continue
        if l[0] == "v":
            texto = texto + "i"
            del l[0]
            continue
        if l[0] == "j":
            texto = texto + "w"
            del l[0]
            continue
        if l[0] == "w":
            texto = texto + "j"
            del l[0]
            continue
        if l[0] == "k":
            texto = texto + "x"
            del l[0]
            continue
        if l[0] == "x":
            texto = texto + "k"
            del l[0]
            continue
        if l[0] == "l":
            texto = texto + "y"
            del l[0]
            continue
        if l[0] == "y":
            texto = texto + "l"
            del l[0]
            continue
        if l[0] == "m":
            texto = texto + "z"
            del l[0]
            continue
        if l[0] == "z":
            texto = texto + "m"
            del l[0]
            continue
    return (texto)