def rot13(palabra):
    lista = []

    for letra in palabra:
        if letra == "a":
            lista.append("n")
        elif letra == "b":
            lista.append("o")
        elif letra == "c":
            lista.append("p")
        elif letra == "d":
            lista.append("q")
        elif letra == "e":
            lista.append("r")
        elif letra == "f":
            lista.append("s")
        elif letra == "g":
            lista.append("t")
        elif letra == "h":
            lista.append("u")
        elif letra == "i":
            lista.append("v")
        elif letra == "j":
            lista.append("w")
        elif letra == "k":
            lista.append("x")
        elif letra == "l":
            lista.append("y")
        elif letra == "m":
            lista.append("z")
        elif letra == "n":
            lista.append("a")
        elif letra == "o":
            lista.append("b")
        elif letra == "p":
            lista.append("c")
        elif letra == "q":
            lista.append("d")
        elif letra == "r":
            lista.append("e")
        elif letra == "s":
            lista.append("f")
        elif letra == "t":
            lista.append("g")
        elif letra == "u":
            lista.append("h")
        elif letra == "v":
            lista.append("i")
        elif letra == "w":
            lista.append("j")
        elif letra == "x":
            lista.append("k")
        elif letra == "y":
            lista.append("l")
        elif letra == "z":
            lista.append("m")
        elif letra == (" "):
            lista.append(" ")
        else:
            letra == ","
            lista.append(",")
        resultado = "".join(lista)
    return resultado
   

