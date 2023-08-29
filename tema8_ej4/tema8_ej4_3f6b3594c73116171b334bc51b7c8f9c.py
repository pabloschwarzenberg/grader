def rot13(palabra):
    trad=""
    for i in palabra:
        if i == "a":
            trad=trad + "n"
        if i == "b":
            trad= trad + "o"
        if i== "c":
            trad =trad + "p"
        if i == "d":
            trad= trad+ "q"
        if i == "e":
            trad = trad+ "r"
        if i == "f":
            trad = trad + "s"
        if i == "g":
            trad = trad +"t"
        if i == "h":
            trad = trad +"u"
        if i == "i":
            trad = trad +"v"
        if i == "j":
            trad = trad +"w"
        if i == "k":
            trad = trad +"x"
        if i == "l":
            trad = trad +"y"
        if i == "m":
            trad = trad +"z"
        if i == "n":
            trad = trad +"a"
        if i == "o":
            trad = trad +"b"
        if i == "p":
            trad = trad +"c"
        if i == "q":
            trad = trad +"d"
        if i == "r":
            trad = trad +"e"
        if i == "s":
            trad = trad +"f"
        if i == "t":
            trad = trad +"g"
        if i == "u":
            trad = trad +"h"
        if i == "v":
            trad = trad +"i"
        if i == "w":
            trad = trad +"j"
        if i == "x":
            trad = trad +"k"
        if i == "y":
            trad = trad +"l"
        if i == "z":
            trad = trad +"m"
    return trad
           