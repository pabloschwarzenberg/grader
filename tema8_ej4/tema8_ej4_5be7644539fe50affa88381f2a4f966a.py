def rot13(palabra):
    encriptado = ""
    for letra in palabra:
        if letra == "a":
            encriptado = encriptado + "n"
        elif letra == "b":
            encriptado = encriptado + "o"
        elif letra == "c":
            encriptado = encriptado + "p"
        elif letra == "d":
            encriptado = encriptado + "q"
        elif letra == "e":
            encriptado = encriptado + "r"
        elif letra == "f":
            encriptado = encriptado + "s"
        elif letra == "g":
            encriptado = encriptado + "t"
        elif letra == "h":
            encriptado = encriptado + "u"
        elif letra == "i":
            encriptado = encriptado + "v"
        elif letra == "j":
            encriptado = encriptado + "w"
        elif letra == "k":
            encriptado = encriptado + "x"
        elif letra == "l":
            encriptado = encriptado + "y"
        elif letra == "m":
            encriptado = encriptado + "z"
        elif letra == "n":
            encriptado = encriptado + "a"
        elif letra == "o":
            encriptado = encriptado + "b"
        elif letra == "p":
            encriptado = encriptado + "c"
        elif letra == "q":
            encriptado = encriptado + "d"
        elif letra == "r":
            encriptado = encriptado + "e"
        elif letra == "s":
            encriptado = encriptado + "f"
        elif letra == "t":
            encriptado = encriptado + "g"
        elif letra == "u":
            encriptado = encriptado + "h"
        elif letra == "v":
            encriptado = encriptado + "i"
        elif letra == "w":
            encriptado = encriptado + "j"
        elif letra == "x":
            encriptado = encriptado + "k"
        elif letra == "y":
            encriptado = encriptado + "l"
        elif letra == "z":
            encriptado = encriptado + "m"
    return encriptado
           