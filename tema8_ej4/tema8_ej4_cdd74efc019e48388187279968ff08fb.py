def rot13(palabra):
    lista = []
    for i in range(0, len(palabra)):
        lista.append(palabra[i])

    for k in range(0, len(palabra)):
        if lista[k] == "a":
            lista[k] = "n"
        elif lista[k] == "b":
            lista[k] = "o"
        elif lista[k] == "c":
            lista[k] = "p"
        elif lista[k] == "d":
            lista[k] = "q"
        elif lista[k] == "e":
            lista[k] = "r"
        elif lista[k] == "f":
            lista[k] = "s"
        elif lista[k] == "g":
            lista[k] = "t"
        elif lista[k] == "h":
            lista[k] = "u"
        elif lista[k] == "i":
            lista[k] = "v"
        elif lista[k] == "j":
            lista[k] = "w"
        elif lista[k] == "k":
            lista[k] = "x"
        elif lista[k] == "l":
            lista[k] = "y"
        elif lista[k] == "m":
            lista[k] = "z"
        elif lista[k] == "n":
            lista[k] = "a"
        elif lista[k] == "o":
            lista[k] = "b"
        elif lista[k] == "p":
            lista[k] = "c"
        elif lista[k] == "q":
            lista[k] = "d"
        elif lista[k] == "r":
            lista[k] = "e"
        elif lista[k] == "s":
            lista[k] = "f"
        elif lista[k] == "t":
            lista[k] = "g"
        elif lista[k] == "u":
            lista[k] = "h"
        elif lista[k] == "v":
            lista[k] = "i"
        elif lista[k] == "w":
            lista[k] = "j"
        elif lista[k] == "x":
            lista[k] = "k"
        elif lista[k] == "y":
            lista[k] = "l"
        elif lista[k] == "z":
            lista[k] = "m"


    return "".join(lista)
    pass
