def rot13(palabra):
    l=[]
    for i in (palabra):
        if i == "a":
            l.append("n")
        if i == "b":
            l.append("o")
        if i == "c":
            l.append("p")
        if i == "d":
            l.append("q")
        if i == "e":
            l.append("r")
        if i == "f":
            l.append("s")
        if i == "g":
            l.append("t")
        if i == "h":
            l.append("u")
        if i == "i":
            l.append("v")
        if i == "j":
            l.append("w")
        if i == "k":
            l.append("x")
        if i == "l":
            l.append("y")
        if i == "m":
            l.append("z")
        if i == "n":
            l.append("a")
        if i == "o":
            l.append("b")
        if i == "p":
            l.append("c")
        if i == "q":
            l.append("d")
        if i == "r":
            l.append("e")
        if i == "s":
            l.append("f")
        if i == "t":
            l.append("g")
        if i == "u":
            l.append("h")
        if i == "v":
            l.append("i")
        if i == "w":
            l.append("j")
        if i == "x":
            l.append("k")
        if i == "y":
            l.append("l")
        if i == "z":
            l.append("m")
        b= "".join(l)              
    return b

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           