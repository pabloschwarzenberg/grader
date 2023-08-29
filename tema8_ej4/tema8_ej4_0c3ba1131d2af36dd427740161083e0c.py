def rot13(palabra):
    a = len(palabra)
    
    i = 0

    j = []
    while (i < a):


        if (palabra[i] == "a"):


            j.append("n")
            
        elif (palabra[i] == "b"):
            print(palabra[i])
            j.append("o")
        elif (palabra[i] == "c"):

            j.append("p")
        elif (palabra[i] == "d"):

            j.append("q")
        elif (palabra[i] == "e"):

            j.append("r")
        elif (palabra[i] == "f"):

            j.append("s")
        elif (palabra[i] == "g"):

            j.append("t")
        elif (palabra[i] == "h"):

            j.append("u")
        elif (palabra[i] == "i"):

            j.append("v")
        elif (palabra[i] == "j"):

            j.append("w")
        elif (palabra[i] == "k"):

            j.append("x")
        elif (palabra[i] == "l"):

            j.append("y")
        elif (palabra[i] == "m"):

            j.append("z")
        elif (palabra[i] == "n"):

            j.append("a")
        elif (palabra[i] == "o"):

            j.append("b")
        elif (palabra[i] == "p"):

            j.append("c")
        elif (palabra[i] == "q"):

            j.append("d")
        elif (palabra[i] == "r"):

            j.append("e")
        elif (palabra[i] == "s"):

            j.append("f")
        elif (palabra[i] == "t"):

            j.append("g")
        elif (palabra[i] == "u"):

            j.append("h")
        elif (palabra[i] == "v"):

            j.append("i")
        elif (palabra[i] == "w"):

            j.append("j")
        elif (palabra[i] == "x"):

            j.append("k")
        elif (palabra[i] == "y"):

            j.append("l")
        elif (palabra[i] == "z"):

            j.append("m")
        i = i + 1
    string = "".join(j)
    return string
print(rot13("hola"))
