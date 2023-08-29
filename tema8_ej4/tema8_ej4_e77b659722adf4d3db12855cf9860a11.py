def rot13(palabra):

    lista = []
    
    for i in palabra:
        lista.append(i)
        
    lista_2 = []
    
    for b in lista:
        if b == "a":
            lista_2.append("n")
        if b == "b":
            lista_2.append("o")
        if b == "c":
            lista_2.append("p")
        if b == "d":
            lista_2.append("Q")
        if b == "e":
            lista_2.append("r")
        if b == "f":
            lista_2.append("s")
        if b == "g":
            lista_2.append("t")
        if b == "h":
            lista_2.append("u")
        if b == "i":
            lista_2.append("v")
        if b == "j":
            lista_2.append("w")
        if b == "k":
            lista_2.append("x")
        if b == "l":
            lista_2.append("y")
        if b == "m":
            lista_2.append("z")
        if b == "n":
            lista_2.append("a")
        if b == "o":
            lista_2.append("b")
        if b == "p":
            lista_2.append("c")
        if b == "q":
            lista_2.append("d")
        if b == "r":
            lista_2.append("e")
        if b == "s":
            lista_2.append("f")
        if b == "t":
            lista_2.append("g")
        if b == "u":
            lista_2.append("h")
        if b == "v":
            lista_2.append("i")
        if b == "w":
            lista_2.append("j")
        if b == "x":
            lista_2.append("k")
        if b == "y":
            lista_2.append("l")
        if b == " ":
            lista_2.append(" ")
            
        else:
            if b == "z":
                lista_2.append("m")
    
    p=""
    for x in lista_2:
        p= p + x
    return(p)

        
letra = input("Ingrese: ")
print(rot13(letra))