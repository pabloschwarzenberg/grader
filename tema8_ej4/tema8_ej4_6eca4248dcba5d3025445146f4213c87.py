def rot13(a):
    i=0
    lista=[]
    while i<len(a):
        if a[i]=="a":
            lista.append("n")
        if a[i]=="b":
            lista.append("o")
        if a[i]=="c":
            lista.append("p")
        if a[i]=="d":
            lista.append("q")
        if a[i]=="e":
            lista.append("r")
        if a[i]=="f":
            lista.append("s")
        if a[i]=="g":
            lista.append("t")
        if a[i]=="h":
            lista.append("u")
        if a[i]=="i":
            lista.append("v")
        if a[i]=="j":
            lista.append("w")
        if a[i]=="k":
            lista.append("x")
        if a[i]=="l":
            lista.append("y")
        if a[i]=="m":
            lista.append("z")
        if a[i]=="n":
            lista.append("a")
        if a[i]=="o":
            lista.append("b")
        if a[i]=="p":
            lista.append("c")
        if a[i]=="q":
            lista.append("d")
        if a[i]=="r":
            lista.append("e")
        if a[i]=="s":
            lista.append("f")
        if a[i]=="t":
            lista.append("g")
        if a[i]=="u":
            lista.append("h")
        if a[i]=="v":
            lista.append("i")
        if a[i]=="w":
            lista.append("j")
        if a[i]=="x":
            lista.append("k")
        if a[i]=="y":
            lista.append("l")
        if a[i]=="z":
            lista.append("m")
        i=i+1
    return "".join(lista)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           