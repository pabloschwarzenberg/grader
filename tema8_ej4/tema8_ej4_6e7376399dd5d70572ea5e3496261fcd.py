def rot13(palabra):
    cesar=""
    for i in palabra:
        if i == "a" or i == "A":
            cesar+="n"
        if i == "b" or i == "B":
            cesar+="o"
        if i == "c" or i == "C":
            cesar+="p"
        if i == "d" or i == "D":
            cesar+="q"
        if i == "e" or i == "E":
            cesar+="r"
        if i == "f" or i == "F":
            cesar+="s"
        if i == "g" or i == "G":
            cesar+="t"
        if i == "h" or i == "H":
            cesar+="u"
        if i == "i" or i == "I":
            cesar+="v"
        if i == "j" or i == "J":
            cesar+="w"
        if i == "k" or i == "K":
            cesar+="x"
        if i == "l" or i == "L":
            cesar+="y"
        if i == "m" or i == "M":
            cesar+="z"
        if i == "n" or i == "N":
            cesar+="a"
        if i == "o" or i == "O":
            cesar+="b"
        if i == "p" or i == "P":
            cesar+="c"
        if i == "q" or i == "Q":
            cesar+="d"
        if i == "r" or i == "R":
            cesar+="e"
        if i == "s" or i == "S":
            cesar+="f"
        if i == "t" or i == "T":
            cesar+="g"
        if i == "u" or i == "U":
            cesar+="h"
        if i == "v" or i == "V":
            cesar+="i"
        if i == "w" or i == "W":
            cesar+="j"
        if i == "x" or i == "X":
            cesar+="k"
        if i == "y" or i == "Y":
            cesar+="l"
        if i == "z" or i == "Z":
            cesar+="m"
    return cesar 
           