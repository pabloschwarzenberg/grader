def rot13(palabra):
    PALABRA = list(palabra)
    q = 0
    while q < len(PALABRA):

        if PALABRA[q] == "a":
            PALABRA[q] = "n"
        elif PALABRA[q] == "b":
            PALABRA[q] = "o"
        elif PALABRA[q] == "c":
            PALABRA[q] = "p"
        elif PALABRA[q] == "d":
            PALABRA[q] = "q"
        elif PALABRA[q] == "e":
            PALABRA[q] = "r"
        elif PALABRA[q] == "f":
            PALABRA[q] = "s"
        elif PALABRA[q] == "g":
            PALABRA[q] = "t"
        elif PALABRA[q] == "h":
            PALABRA[q] = "u"
        elif PALABRA[q] == "i":
            PALABRA[q] = "v"
        elif PALABRA[q] == "j":
            PALABRA[q] = "w"
        elif PALABRA[q] == "k":
            PALABRA[q] = "x"
        elif PALABRA[q] == "l":
            PALABRA[q] = "y"
        elif PALABRA[q] == "m":
            PALABRA[q] = "z"
        elif PALABRA[q] == "n":
            PALABRA[q] = "a"
        elif PALABRA[q] == "o":
            PALABRA[q] = "b"
        elif PALABRA[q] == "p":
            PALABRA[q] = "c"
        elif PALABRA[q] == "q":
            PALABRA[q] = "d"
        elif PALABRA[q] == "r":
            PALABRA[q] = "e"
        elif PALABRA[q] == "s":
            PALABRA[q] = "f"
        elif PALABRA[q] == "t":
            PALABRA[q] = "g"
        elif PALABRA[q] == "u":
            PALABRA[q] = "h"
        elif PALABRA[q] == "v":
            PALABRA[q] = "i"
        elif PALABRA[q] == "w":
            PALABRA[q] = "j"
        elif PALABRA[q] == "x":
            PALABRA[q] = "k"
        elif PALABRA[q] == "y":
            PALABRA[q] = "l"
        elif PALABRA[q] == "z":
            PALABRA[q] = "m"
        else:
            PALABRA[q] = PALABRA[q]
        q = q + 1
    prueba = ''.join(PALABRA)
    return prueba
