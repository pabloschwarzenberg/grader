def rot13(palabra):
    palabra1 = ""
    for n in palabra:
        
        if n == "a":
            palabra1 += n.replace("a","n")

        elif n == "b":
            palabra1 += n.replace("b","o")

        elif n == "c":
            palabra1 += n.replace("c","p")

        elif n == "d":
            palabra1 += n.replace("d","q")

        elif n == "e":
            palabra1 += n.replace("e","r")

        elif n == "f":
            palabra1 += n.replace("f","s")

        elif n == "g":
            palabra1 += n.replace("g","t")

        elif n == "h":
            palabra1 += n.replace("h","u")

        elif n == "i":
            palabra1 += n.replace("i","v")

        elif n == "j":
            palabra1 += n.replace("j","w")

        elif n == "k":
            palabra1 += n.replace("k","x")

        elif n == "l":
            palabra1 += n.replace("l","y")

        elif n == "m":
            palabra1 += n.replace("m","z")

        elif n == "n":
            palabra1 += n.replace("n","a")

        elif n == "o":
            palabra1 += n.replace("o","b")

        elif n == "p":
            palabra1 += n.replace("p","c")

        elif n == "q":
            palabra1 += n.replace("q","d")

        elif n == "r":
            palabra1 += n.replace("r","e")

        elif n == "s":
            palabra1 += n.replace("s","f")

        elif n == "t":
            palabra1 += n.replace("t","g")

        elif n == "u":
            palabra1 += n.replace("u","h")

        elif n == "v":
            palabra1 += n.replace("v","i")

        elif n == "w":
            palabra1 += n.replace("w","j")

        elif n == "x":
            palabra1 += n.replace("x","k")

        elif n == "y":
            palabra1 += n.replace("y","l")

        elif n == "z":
            palabra1 += n.replace("z","m")

    return palabra1


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           