def rot13(palabra):
    palabra =list(palabra)
    for i in range(0,len(palabra)):
        if palabra[i] == "a":
            palabra[i] = "n"
        elif palabra[i] == "A":
            palabra[i] = "N"
        elif palabra[i] == "b":
            palabra[i] = "o"
        elif palabra[i] == "B":
            palabra[i] = "O"
        elif palabra[i] == "c":
            palabra[i] = "p"
        elif palabra[i] == "C":
            palabra[i] = "P"
        elif palabra[i] == "d":
            palabra[i] = "q"
        elif palabra[i] == "D":
            palabra[i] = "Q"
        elif palabra[i] == "e":
            palabra[i] = "r"
        elif palabra[i] == "E":
            palabra[i] = "R"
        elif palabra[i] == "f":
            palabra[i] = "s"
        elif palabra[i] == "F":
            palabra[i] = "S"
        elif palabra[i] == "g":
            palabra[i] = "t"
        elif palabra[i] == "G":
            palabra[i] = "T"
        elif palabra[i] == "h":
            palabra[i] = "u"
        elif palabra[i] == "H":
            palabra[i] = "U"
        elif palabra[i] == "i":
            palabra[i] = "v"
        elif palabra[i] == "I":
            palabra[i] = "V"
        elif palabra[i] == "j":
            palabra[i] = "w"
        elif palabra[i] == "J":
            palabra[i] = "W"
        elif palabra[i] == "k":
            palabra[i] = "x"
        elif palabra[i] == "K":
            palabra[i] = "X"
        elif palabra[i] == "l":
            palabra[i] = "y"
        elif palabra[i] == "L":
            palabra[i] = "Y"
        elif palabra[i] == "m":
            palabra[i] = "z"
        elif palabra[i] == "m":
            palabra[i] = "Z"
        elif palabra[i] == "n":
            palabra[i] = "a"
        elif palabra[i] == "N":
            palabra[i] = "A"
        elif palabra[i] == "o":
            palabra[i] = "b"
        elif palabra[i] == "O":
            palabra[i] = "B"
        elif palabra[i] == "p":
            palabra[i] = "c"
        elif palabra[i] == "P":
            palabra[i] = "C"
        elif palabra[i] == "q":
            palabra[i] = "d"
        elif palabra[i] == "Q":
            palabra[i] = "D"
        elif palabra[i] == "r":
            palabra[i] = "e"
        elif palabra[i] == "R":
            palabra[i] = "E"
        elif palabra[i] == "s":
            palabra[i] = "f"
        elif palabra[i] == "S":
            palabra[i] = "F"
        elif palabra[i] == "t":
            palabra[i] = "g"
        elif palabra[i] == "T":
            palabra[i] = "G"
        elif palabra[i] == "u":
            palabra[i] = "h"
        elif palabra[i] == "U":
            palabra[i] = "H"
        elif palabra[i] == "v":
            palabra[i] = "i"
        elif palabra[i] == "V":
            palabra[i] = "I"
        elif palabra[i] == "W":
            palabra[i] = "J"
        elif palabra[i] == "j":
            palabra[i] = "w"
        elif palabra[i] == "X":
            palabra[i] = "K"
        elif palabra[i] == "x":
            palabra[i] = "k"
        elif palabra[i] == "y":
            palabra[i] = "l"
        elif palabra[i] == "Y":
            palabra[i] = "L"
        elif palabra[i] == "Z":
            palabra[i] = "M"
        elif palabra[i] == "z":
            palabra[i] = "m"
    return "".join(palabra)