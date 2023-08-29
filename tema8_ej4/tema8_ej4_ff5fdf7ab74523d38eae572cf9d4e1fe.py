def rot13(palabra):
    cesar=[]
    for i in palabra:
        if i== "a":
            cesar.append("n")
        if i== "b":
            cesar.append("o")
        if i== "c":
            cesar.append("p")
        if i== "d":
            cesar.append("q")
        if i== "e":
            cesar.append("r")
        if i== "f":
            cesar.append("s")
        if i== "g":
            cesar.append("t")
        if i== "h":
            cesar.append("u")
        if i== "i":
            cesar.append("v")
        if i== "j":
            cesar.append("w")
        if i== "k":
            cesar.append("x")
        if i== "l":
            cesar.append("y")
        if i== "m":
            cesar.append("z")
        if i== "n":
            cesar.append("a")
        if i== "o":
            cesar.append("b")
        if i== "p":
            cesar.append("c")
        if i== "q":
            cesar.append("d")
        if i== "r":
            cesar.append("e")
        if i== "s":
            cesar.append("f")
        if i== "t":
            cesar.append("g")
        if i== "u":
            cesar.append("h")
        if i== "v":
            cesar.append("i")
        if i== "w":
            cesar.append("j")
        if i== "x":
            cesar.append("k")
        if i== "y":
            cesar.append("l")
        if i== "z":
            cesar.append("m")
            
        julio="".join(cesar)
        
    return julio
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           