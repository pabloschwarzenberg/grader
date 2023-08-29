def rot13(palabra):
    rot13 = ""
    for i in palabra:
        if i == "a":
            rot13 = rot13 + "n"
        if i == "b":
            rot13 = rot13 + "o"
        if i == "c":
            rot13 = rot13 + "p"
        if i == "d":
            rot13 = rot13 + "q"
        if i == "e":
            rot13 = rot13 + "r"
        if i == "f":
            rot13 = rot13 + "s"
        if i == "g":
            rot13 = rot13 + "t"
        if i == "h":
            rot13 = rot13 + "u" 
        if i == "i":
            rot13 = rot13 + "v"
        if i == "j":
            rot13 = rot13 + "w"
        if i == "k":
            rot13 = rot13 + "x"
        if i == "l":
            rot13 = rot13 + "y"
        if i == "m":
            rot13 = rot13 + "z"
        if i == "n":
            rot13 = rot13 + "a"
        if i == "o":
            rot13 = rot13 + "b"
        if i == "p":
            rot13 = rot13 + "c"
        if i == "q":
            rot13 = rot13 + "d"
        if i == "r":
            rot13 = rot13 + "e"
        if i == "s":
            rot13 = rot13 + "f"
        if i == "t":
            rot13 = rot13 + "g"
        if i == "u":
            rot13 = rot13 + "h" 
        if i == "v":
            rot13 = rot13 + "i"
        if i == "w":
            rot13 = rot13 + "j"
        if i == "x":
            rot13 = rot13 + "k"
        if i == "y":
            rot13 = rot13 + "l" 
        if i == "z":
            rot13 = rot13 + "m"
        if i == " ":
            rot13 = rot13 + i

    return rot13

           
           