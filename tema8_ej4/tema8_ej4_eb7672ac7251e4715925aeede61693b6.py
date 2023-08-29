def rot13(palabra):

    
    lista=[]
    for i in palabra:
        
        if i=="a":
            lista.append("n")  
        if i=="b":
            lista.append("o")
        if i=="c":
            lista.append("p")
        if i=="d":
            lista.append("q")
        if i=="e":
            lista.append("r")
        if i=="f":
            lista.append("s")
        if i=="g":
            lista.append("t")
        if i=="h":
            lista.append("u")
        if i=="i":
            lista.append("v")
        if i=="j":
            lista.append("w")
        if i=="k":
            lista.append("x")
        if i=="l":
            lista.append("y")
        if i=="m":
            lista.append("z")
        if i=="n":
            lista.append("a")
        if i=="o":
            lista.append("b")
        if i=="p":
            lista.append("c")
        if i=="q":
            lista.append("d")
        if i=="r":
            lista.append("e")
        if i=="s":
            lista.append("f")
        if i=="t":
            lista.append("g")
        if i=="u":
            lista.append("h")
        if i=="v":
            lista.append("i")
        if i=="w":
            lista.append("j")
        if i=="x":
            lista.append("k")
        if i=="y":
            lista.append("l")
        if i=="z":
            lista.append("m")

    palabra13="".join(lista)
    return palabra13
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           